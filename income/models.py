from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator
from autoslug import AutoSlugField
# Create your models here.


class Source(models.Model):
    name = models.CharField(max_length=255)
    
    
    class Meta:
        verbose_name='Income Source'
        verbose_name_plural='Income Source'
    
    def __str__(self):
        return str(self.name) 
    
    


class Income(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=800)
    slug= AutoSlugField(populate_from='description',unique_with=['income_date','amount','source','created'])
    amount = models.FloatField(validators=[MinValueValidator(limit_value=0,message="sorry your expenses can't be less than zero")])
    income_date = models.DateField(help_text='yyyy-mm-dd')
    source = models.ForeignKey(Source,on_delete=models.CASCADE) 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return str(self.source) +' ' +str(self.description)