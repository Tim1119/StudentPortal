from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserPreferences(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    currency = models.CharField(max_length=55,blank=True,null=True) 

    def __str__(self):
        return str(self.user) + str(self.currency)
