from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile


@login_required
def user_profile(request, user):
    """ A view to return the profile page """

    if not request.user.is_authenticated:
        return redirect(reverse('home'))

    context = {
        'user': user,
    }

    try:
        get_user = get_object_or_404(User, username=user)

        user_profile = get_object_or_404(UserProfile, user=get_user)

        context = {
                'user_profile': user_profile,
                'user': user,
            }

        return render(request, 'profiles/profile.html', context)
    except Exception as e:
        return render(request, 'profiles/profile.html', context)
