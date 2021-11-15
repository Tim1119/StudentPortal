from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserPreferences

@receiver(post_save,sender=User)
def post_create_settings(sender,instance,created,**kwargs):
    if created:
        UserPreferences.objects.create(user=instance)
        