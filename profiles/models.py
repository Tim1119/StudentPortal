from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.core.validators import FileExtensionValidator

# Create your models here.



class Profile(models.Model):
    owner = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(default='avatar.png',upload_to='profile-images',validators=[FileExtensionValidator(['png','jpg','jpeg'],message='File can only be image type')])
    company = models.CharField(max_length=100,blank=True,null=True)
    job = models.CharField(max_length=100,blank=True,null=True) 
    country =  models.CharField(max_length=100,blank=True,null=True) 
    address =  models.CharField(max_length=100,blank=True,null=True) 
    about = models.TextField(blank=True,null=True)
    slug= AutoSlugField(populate_from='owner',unique_with=['created','address','company'])
    twitter = models.URLField(blank=True,null=True)
    facebook = models.URLField(blank=True,null=True)
    instagram = models.URLField(blank=True,null=True)
    linkedin = models.URLField(blank=True,null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.owner) + '- profile'
    
    @property
    def profile_pic_url(self):
        try:
            url = self.avatar.url 
        except:
            url ='' 
        return url
    
    
    class Meta:
        
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'
    
