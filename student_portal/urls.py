from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('expenses.urls',namespace='expenses')),
    #path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include('authentication.urls',namespace='authentication')),
    path('settings/',include('settings.urls',namespace='settings')),
]
