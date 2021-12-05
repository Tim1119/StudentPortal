from django.urls import path
from .views import SearchDictionaryView,DictionaryView

app_name = 'dictionary'

urlpatterns = [
    
    path('', DictionaryView.as_view(),name='dictionary'),
    path('search-dictionary/', SearchDictionaryView,name='search-dictionary'),
   
    
]