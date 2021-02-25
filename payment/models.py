from django.db import models
from django.contrib.auth.models import User


class PaidMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(max_length=80,
                                      null=False, blank=False)
    end_date = models.DateTimeField(max_length=80,
                                    null=False, blank=False)
    subscription = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
