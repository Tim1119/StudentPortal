from django.urls import path
from .views import SearchBookView,BookView

app_name = 'books'

urlpatterns = [
    
    path('', BookView.as_view(),name='book'),
    path('search-book/', SearchBookView,name='search-book'),
   
    
]