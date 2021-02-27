from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    A model to save or edit user profiles
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
