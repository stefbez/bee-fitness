from django.contrib import admin
from .models import ExercisePlan
# Register your models here.


class ExercisePlanAdmin(admin.ModelAdmin):
    """ Premium User Admin """
    list_display = (
        'user',
        'title',
        'warmup_time',
        'warmup_instructions',
        'main_exercise_time',
        'exercise_instructions',
        'cooldown_time',
        'cooldown_instructions',
    )


admin.site.register(ExercisePlan, ExercisePlanAdmin)
