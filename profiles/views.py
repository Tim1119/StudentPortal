from django.shortcuts import render
from django.views.generic import UpdateView,TemplateView
from profiles.models import Profile
from .forms import ProfileForm
from .models import Profile
from django.urls import reverse_lazy,reverse


# Create your views here.

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile.html' 
    success_message = "Profile was updated sucessfully"
    context_object_name='profile'
    
    def get_success_url(self):
        if 'slug' in self.kwargs:
            slug = self.kwargs['slug']
        return reverse('profile:view-update-profile', kwargs={'slug': slug})