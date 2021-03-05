from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ExercisePlan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    minutes_needed = models.IntegerField
    exercise_instructions = models.TextField(max_length=100)

    def __str__(self):
        return self.user
