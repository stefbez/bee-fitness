from django.shortcuts import render


def members(request):
    """ A view to return the index page """
    return render(request, 'members/members.html')
