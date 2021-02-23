from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def members(request):
    """ A view to return the index page """
    return render(request, 'members/members.html')
