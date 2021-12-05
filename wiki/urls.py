from django.urls import path
from .views import SearchWikipediaView,WikipediaView

app_name = 'wikipedia'

urlpatterns = [
    
    path('', WikipediaView.as_view(),name='wikipedia'),
    path('search-wikipedia/', SearchWikipediaView,name='search-wikipedia'),
   
    
]