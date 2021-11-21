from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator
from autoslug import AutoSlugField
from django.core.exceptions import ValidationError
# Create your models here.


class Source(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    slug  = AutoSlugField(populate_from='name',unique_with=['created'])
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Income Source'
        verbose_name_plural = 'Income Source'
        ordering = ['-created']
        unique_together = ('name','owner')
    
    def __str__(self):
        return str(self.name) 
    
    def validate_unique(self,exclude=None):
        try:
            super(Source,self).validate_unique()
        except ValidationError as e:
            raise ValidationError("Ooops, "+ str(self.name)+" income source already exists.")
    
    


class Income(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=800)
    slug  = AutoSlugField(populate_from='description',unique_with=['owner','source','created','updated'])
    amount = models.FloatField(validators=[MinValueValidator(limit_value=0,message="sorry your expenses can't be less than zero")])
    income_date = models.DateField(help_text='yyyy-mm-dd')
    source = models.ForeignKey(Source,on_delete=models.CASCADE) 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-income_date']
        unique_together = ('amount','description','source','owner')
        
    def __str__(self):
        return str(self.source) +' ' +str(self.description) 
    
    def validate_unique(self,exclude=None):
        try:
            super(Income,self).validate_unique()
        except ValidationError as e:
            raise ValidationError("Oops, "+ str(self.amount) +" with same source and description already exists")
    
