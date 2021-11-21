from django.urls import path
from .views import (
IncomeView,AddIncomeView,UpdateIncomeView,DeleteIncomeView,SearchIncome,ViewIncomeSummary,
 income_source_summary_json,search_by_date,search_within_date_range,export_csv,export_pdf,
 IncomeSourceView,AddIncomeSourceView,UpdateIncomeSourceView,DeleteIncomeSourceView
 )

app_name = 'income'

urlpatterns = [

    
    path('',IncomeView.as_view(),name='income'),
    path('add-income/',AddIncomeView.as_view(),name='add-income'),
    path('search-income/',SearchIncome,name='search-income'),
    path('update-income/<slug>/',UpdateIncomeView.as_view(),name='update-income'),
    path('delete-income/<slug>/',DeleteIncomeView.as_view(),name='delete-income'),
    path('income-summary-json/',income_source_summary_json,name='income-summary-json'),
    path('income-summary/',ViewIncomeSummary.as_view(),name='income-summary'),
    path('search-by-date/',search_by_date,name='search-by-date'),
    path('search-within-date/',search_within_date_range,name='search-within-date'),
    path('export-csv/',export_csv,name='export-csv'),
    path('export-pdf/',export_pdf,name='export-pdf'),
    
    
    path('sources/',IncomeSourceView.as_view(),name='sources'),
    path('add-income-source/',AddIncomeSourceView.as_view(),name='add-income-source'),
    path('update-income-source/<slug>/',UpdateIncomeSourceView.as_view(),name='update-income-source'),
    path('delete-income-source/<slug>/',DeleteIncomeSourceView.as_view(),name='delete-income-source'),


]