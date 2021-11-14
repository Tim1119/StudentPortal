from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Expense(models.Model):
    owner = models.OneToOneField(user=User,on_delete=models.CASCADE)
    amount = models.FloatField(min_value=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_created_add=True)
    category = models.CharField(max_length=255) 
    
    class Meta:
        ordering = ['-created']
    
    
    def __str__(self):
        return self.owner + str(self.category) + 'expenses' 
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.name) + 'category'