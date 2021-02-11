from django.shortcuts import render


def profiles(request):
    """ A view to return the index page """
    return render(request, 'profiles/profile.html')
