from django.db import models
from profiles.models import Profile
from django.core.exceptions import ValidationError
from autoslug import AutoSlugField
# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=60)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE)
    slug  = AutoSlugField(populate_from='task',unique_with=['owner','created'])
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.task) + ' todo ' + str(self.owner)
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Todo'
        verbose_name_plural = 'Todo'
        unique_together = ('task','owner')
        
    def validate_unique(self,exclude=None):
        try:
            super(Todo,self).validate_unique()
        except ValidationError as e:
            raise ValidationError("Oops, this todo item already exists")
    
    def all_todo_counts(self):
        return self.objects.all().count()