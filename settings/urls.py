from django.urls import path
from .views import settingsView,saveUserSettings

app_name='settings'

urlpatterns = [
   path('',settingsView,name='settings'),
   path('save_settings/',saveUserSettings,name='save-settings')
]
