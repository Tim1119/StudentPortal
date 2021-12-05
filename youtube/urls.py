from django.urls import path
from .views import SearchYoutubeView,YoutubeView

app_name = 'youtube'

urlpatterns = [
    
    path('', YoutubeView.as_view(),name='youtube'),
    path('search-youtube/', SearchYoutubeView,name='search-youtube'),
   
    
]