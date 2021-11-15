from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('expenses/',include('expenses.urls',namespace='expenses')),
    path('accounts/',include('authentication.urls',namespace='authentication')),
    path('settings/',include('settings.urls',namespace='settings')),
    path('income/',include('income.urls',namespace='income')),
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)