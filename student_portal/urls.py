from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from authentication.views import HomeView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('expenses/',include('expenses.urls',namespace='expenses')),
    path('accounts/',include('authentication.urls',namespace='authentication')),
    path('settings/',include('settings.urls',namespace='settings')),
    path('income/',include('income.urls',namespace='income')),
    path('profile/',include('profiles.urls',namespace='profile')),
    path('notes/',include('notes.urls',namespace='notes')),
    path('todo/',include('todo.urls',namespace='todo')),
    path('youtube/',include('youtube.urls',namespace='youtube')),
    path('books/',include('books.urls',namespace='books')),
    path('wikipedia/',include('wiki.urls',namespace='wikipedia')),
    path('dictionary/',include('dictionary.urls',namespace='dictionary')),
   
    path('',HomeView,name='home'),
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)