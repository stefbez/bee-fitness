from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ExercisePlan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    warmup_time = models.IntegerField(default=0, null=False, blank=True)
    warmup_instructions = models.TextField(
        max_length=100, null=False, blank=True)
    main_exercise_time = models.IntegerField(
        default=0)
    exercise_instructions = models.TextField(max_length=100)
    cooldown_time = models.IntegerField(default=0, null=False, blank=True)
    cooldown_instructions = models.TextField(
        max_length=100, null=False, blank=True)

    def __str__(self):
        return self.user.username
