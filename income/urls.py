from django.urls import path
from .views import IncomeView,AddIncomeView,UpdateIncomeView,DeleteIncomeView,SearchIncome

app_name = 'income'

urlpatterns = [

    
    path('',IncomeView.as_view(),name='income'),
    path('add-income/',AddIncomeView.as_view(),name='add-income'),
    path('search-income/',SearchIncome,name='search-income'),
    path('update-income/<slug>/',UpdateIncomeView.as_view(),name='update-income'),
    path('delete-income/<slug>/',DeleteIncomeView.as_view(),name='delete-income'),

]