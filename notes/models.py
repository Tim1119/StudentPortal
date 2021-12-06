from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from profiles.models import Profile
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.utils import timezone



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
        unique_together = ('name','owner')
    
    def __str__(self):
        return str(self.name) 

    def validate_unique(self,exclude=None):
        try:
            super(Note,self).validate_unique()
        except ValidationError as e:
            raise ValidationError("Oops, course with this title belogning to you already exists")
    


class Note(models.Model):
    title =models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,blank=True,null=True,help_text='leave blank if it is a stand alone note')
    note_order = models.IntegerField(blank=True,null=True,help_text='leave blank if it has no order')
    content = RichTextField()
    slug = AutoSlugField(populate_from='title',unique_with=['created','profile','course'])
    #date = models.DateField(default=timezone.now())
    updated =models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title) + ' note'
    
    class Meta:
        ordering = ['-created']
        unique_together = ('title','course','profile')
        
    def validate_unique(self,exclude=None):
        try:
            super(Note,self).validate_unique()
        except ValidationError as e:
            raise ValidationError("Oops, note with this title,in this course, belonging to you already exists")

    def all_notes_counts(self):
        return self.notes.all().count()