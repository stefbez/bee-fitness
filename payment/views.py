from django.shortcuts import render
import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@login_required
def payment(request):
    """ A view to return the index page """
    return render(request, 'payment/payment.html')

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'https://8000-lime-wallaby-so47o6kn.ws-eu03.gitpod.io/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
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
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

@login_required
def success(request):
    return render(request, 'payment/success.html')


@login_required
def cancel(request):
    return render(request, 'payment/cancel.html')
