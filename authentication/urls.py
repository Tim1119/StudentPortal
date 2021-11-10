from django.urls import path
from .views import RegistrationView, LoginView,UserNameValidationView

app_name = 'authentication'

urlpatterns = [

    path('register/',RegistrationView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('validate-username/',UserNameValidationView.as_view(),name='validate_username'),

]
