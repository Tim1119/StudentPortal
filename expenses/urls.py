from django.urls import path
from .views import AddExpenseView

app_name = 'expenses'

urlpatterns = [

    
    path('add-expense/',AddExpenseView.as_view(),name='add-expenses'),
    path('expenses/',AddExpenseView.as_view(),name='expenses'),

]
