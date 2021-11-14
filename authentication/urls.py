from django.urls import path
from .views import RegisterUserView,LoginUser,UserLogoutView,HomeView,VerificationView

app_name = 'authentication'

urlpatterns = [
    path('',HomeView,name='home'),
    path('register/',RegisterUserView.as_view(),name='register'),
    #path('register/',RegistrationView.as_view(),name='register'),
    path('login/',LoginUser.as_view(),name='login'),
    path('logout/',UserLogoutView,name='logout'),
    path('activate/<uidb64>/<token>/',VerificationView.as_view(),name='activate'),

]
