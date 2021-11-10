from django.urls import path
from .views import HomeView,AddExpenseView

app_name = 'expenses'

urlpatterns = [

    path('',HomeView.as_view(),name='home'),
    path('add-expense/',AddExpenseView.as_view(),name='add-expense'),

]
