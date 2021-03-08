from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import ExercisePlan

from datetime import datetime


@login_required
def members(request):
    """ A view to return the members page """
    exercise_plans = ExercisePlan.objects.filter(user=request.user)
    member_user = request.user
    date = datetime.now()
    if exercise_plans:
        context = {
            'member_user': member_user,
            'exercise_plans': exercise_plans,
        }
    else:
        context = {
            'member_user': member_user,
        }
    date = datetime.strftime(date, '%d %B %Y')
    return render(request, 'members/members.html', context)
