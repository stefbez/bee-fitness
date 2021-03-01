from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

from profiles.models import UserProfile


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    first_line_address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class PaidMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(max_length=80,
                                      null=False, blank=False)
    end_date = models.DateTimeField(max_length=80,
                                    null=False, blank=False)
    subscription = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
