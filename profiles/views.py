from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from payment.models import UserInfo
from payment.admin import UserInfoAdmin
from payment.forms import UserInfoForm
from .forms import UserProfileForm


@login_required
def user_profile(request):
    """ A view to return the profile page """

    user_profile = get_object_or_404(UserProfile, user=request.user)
    user_info = UserInfo.objects.filter(user=request.user).first()
    if user_info:
        user = UserInfo.objects.get(user=request.user)
    form = UserProfileForm(instance=user_profile)
    print(form)
    form = UserInfoForm(instance=user)
    if request.method == 'POST':
        print('IF POST WORKS')
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form_data = {
                'first_name': request.POST['first_name'],
                'last_name': request.POST['last_name'],
                'first_line_address': request.POST['first_line_address'],
                'postcode': request.POST['postcode'],
            }

        user = UserInfo.objects.get(user=request.user)
        user_info = UserInfoForm(request.POST, instance=user)

        temp = user_info.save(commit=False)
        temp.user = request.user
        # temp['user'] = request.user
        if user_info.is_valid():
            temp.save()

        return redirect(reverse('user_profile'))

    # user_profile = get_object_or_404(UserProfile, user=get_user)
    # user_info = UserInfoForm
    context = {
            'form': form,
            "user_info": user_info,
            "user_info": form
        }
    if user_info:
        context['user'] = user_info

    return render(request, 'profiles/profile.html', context)
