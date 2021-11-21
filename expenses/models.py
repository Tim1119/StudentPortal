from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from autoslug import AutoSlugField



class ExpenseCategory(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    slug  = AutoSlugField(populate_from='name',unique_with=['created'])
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Category'
        unique_together = ('name','owner')
    
    def __str__(self):
        return str(self.name)
    
    def validate_unique(self,exclude=None):
        try:
            super(ExpenseCategory,self).validate_unique()
        except ValidationError as e:
            raise ValidationError("Ooops, "+ str(self.name)+" expense category already exists ")

    
    
class Expense(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=800)
    slug  = AutoSlugField(populate_from='description',unique_with=['owner','category','created','updated'],unique=True)
    amount = models.FloatField(validators=[MinValueValidator(limit_value=0,message="sorry your expenses can't be less than zero")])
    expense_date = models.DateField(help_text='yyyy-mm-dd')
    category = models.ForeignKey(ExpenseCategory,on_delete=models.CASCADE) 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-expense_date']
        unique_together = ('amount','description','category','owner')
    
    def get_category(self):
        return self.category
    
    def __str__(self):
        return str(self.owner) + ' ' +str(self.category) + ' expenses' 
    
    def validate_unique(self,exclude=None):
        try:
            super(Expense,self).validate_unique()
        except ValidationError as e:
            raise ValidationError("Ooops," + str(self.amount)+ " with same description and category already exists")
    
    

    

    
