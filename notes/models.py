from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from profiles.models import Profile
from ckeditor.fields import RichTextField

class Course(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE)
    slug  = AutoSlugField(populate_from='name',unique_with=['created'])
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Course'
        ordering = ['-created']
    
    def __str__(self):
        return str(self.name) 

    


class Note(models.Model):
    title =models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,blank=True,null=True,help_text='leave blank if it is a stand alone note')
    note_order = models.IntegerField(blank=True,null=True,help_text='leave blank if it has no order')
    content = RichTextField()
    slug = AutoSlugField(populate_from='title',unique_with=['created','profile','course'])
    updated =models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title) + ' note'
    
    class Meta:
        ordering = ['-created']