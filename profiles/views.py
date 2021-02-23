from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
# from .models import UserProfile
# from .forms import UserProfileForm

def user_profile(request):
    """ Display the users profile """
    profile = get_object_or_404(UserProfile, user = request.user)
    return render(request, template, context)
