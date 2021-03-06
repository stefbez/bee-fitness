from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import UserInfo


@receiver(post_save, sender=UserInfo)
def update_on_save(sender, instance, created, **kwargs):
    instance.UserInfo.payment()


@receiver(post_delete, sender=UserInfo)
def update_on_delete(sender, instance, **kwargs):
    instance.UserInfo.payment()
