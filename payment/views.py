from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required

from datetime import datetime
from dateutil.relativedelta import relativedelta

from .models import PaidMember, UserInfo
from .forms import UserInfoForm


import stripe


@login_required
def payment(request):
    """ A view to return the payment page """
    # get the user from the DB
    try:
        user = UserInfo.objects.get(user=request.user)
        form = UserInfoForm(instance=user)
    except UserInfo.DoesNotExist:
        form = UserInfoForm()

    if request.method == 'POST':
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'first_line_address': request.POST['first_line_address'],
            'postcode': request.POST['postcode'],
        }

        try:
            user = UserInfo.objects.get(user=request.user)
            user_info = UserInfoForm(request.POST, instance=user)
        except UserInfo.DoesNotExist:
            user_info = UserInfoForm(request.POST)

        temp = user_info.save(commit=False)
        temp.user = request.user
        temp.save()

        return redirect(reverse('payment'))

    template = 'payment/payment.html'
    user_info = UserInfoForm
    context = {
        "user_info": user_info,
        "user_info": form
        }

    return render(request, template, context)


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'https://bee-fitness.herokuapp.com/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id 
                if request.user.is_authenticated else None,
                success_url=domain_url + 'payment/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'payment/cancel/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': settings.STRIPE_PRICE_ID,
                        'quantity': 1,
                    }
                ]
            )
            request.session['membership_payment_success'] = True
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@login_required
def success(request):
    if 'membership_payment_success' in request.session:
        amount = 599.00
        start_date = datetime.now()
        end_date = start_date + relativedelta(years=1)

        PaidMember.objects.create(
            user=request.user, start_date=start_date,
            end_date=end_date, subscription=True)
        del request.session['membership_payment_success']

        # Format date time to date only
        start_date = datetime.strftime(start_date, '%d %B %Y')
        end_date = datetime.strftime(end_date, '%d %B %Y')

        context = {
            'start_date': start_date,
            'end_date': end_date,
            'amount': amount,
        }

        return render(request, 'payment/success.html', context)

    return redirect(reverse('payment'))


@login_required
def cancel(request):
    return render(request, 'payment/cancel.html')


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    return HttpResponse(status=200)


@staff_member_required
def check_paid_status(request):
    date = datetime.now()
    end_dates = PaidMember.objects.filter(end_date__lte=date)
    end_dates.delete()

    return render(request, 'payment/check-paid-status.html')
