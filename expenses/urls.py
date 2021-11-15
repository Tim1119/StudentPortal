from django.urls import path
from .views import ExpenseView,AddExpenseView,UpdateExpenseView,DeleteExpenseView,SearchExpenses

app_name = 'expenses'

urlpatterns = [

    
    path('',ExpenseView.as_view(),name='expenses'),
    path('add-expense/',AddExpenseView.as_view(),name='add-expenses'),
    path('search-expenses/',SearchExpenses,name='search-expenses'),
    path('update-expense/<slug>/',UpdateExpenseView.as_view(),name='update-expense'),
    path('delete-expense/<slug>/',DeleteExpenseView.as_view(),name='delete-expense'),

]
