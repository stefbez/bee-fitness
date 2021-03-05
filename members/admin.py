from django.contrib import admin

# Register your models here.


class ExercisePlanAdmin(admin.ModelAdmin):
    """ Premium User Admin """
    list_display = (
        'user',
        'title',
        'minutes_needed',
        'exercise_instructions',
    )
