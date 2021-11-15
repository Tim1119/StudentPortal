from django.urls import path
from .views import ProfileUpdateView

app_name = 'profile'

urlpatterns = [
    
    path('update-profile/<slug>/',ProfileUpdateView.as_view(),name='update-profile'),
    
]