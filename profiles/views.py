from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from payment.models import UserInfo
from payment.admin import UserInfoAdmin
from payment.forms import UserInfoForm


@login_required
def user_profile(request, user):
    """ A view to return the profile page """

    get_user = get_object_or_404(user, username=user)

    user = UserInfo.objects.get(user=request.user)
    form = UserInfoForm(instance=user)
    print(form)

    if request.method == 'POST':
        print('IF POST WORKS')
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'phone_number': request.POST['phone_number'],
            'first_line_address': request.POST['first_line_address'],
            'postcode': request.POST['postcode'],
        }

        user = UserInfo.objects.get(user=request.user)
        user_info = UserInfoForm(request.POST, instance=user)

        temp = user_info.save(commit=False)
        temp.user = request.user
            # temp['user'] = request.user
            # if user_info.is_valid():
        temp.save()

        return redirect(reverse('user_profile'))

    user_profile = get_object_or_404(UserProfile, user=get_user)
    user_info = UserInfoForm
    context = {
            'user_profile': user_profile,
            'user': user,
            "user_info": user_info,
            "user_info": form
        }

    return render(request, 'profiles/profile.html', context)
