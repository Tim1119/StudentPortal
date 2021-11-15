from django.shortcuts import render
from django.views.generic import UpdateView
from profiles.models import Profile
from student_portal.profiles.forms import ProfileForm
from .models import Profile
from django.urls import reverse_lazy


# Create your views here.
def ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'update-profile.html' 
    success_message = "Profile was updated sucessfully"
    success_url =  reverse_lazy('income:income') 