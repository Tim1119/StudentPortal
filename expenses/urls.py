from django.urls import path
from .views import (
    ExpenseView,AddExpenseView,UpdateExpenseView,
    DeleteExpenseView,SearchExpenses,expense_category_summary_json,ViewExpenseSummary,search_by_date,
    search_within_date_range,export_csv,export_pdf,ExpenseCategoryView,UpdateExpenseCategoryView
    ,AddExpenseCategoryView,DeleteExpenseCategoryView
    )

app_name = 'expenses'

urlpatterns = [

    
    path('',ExpenseView.as_view(),name='expenses'),
    path('add-expense/',AddExpenseView.as_view(),name='add-expenses'),
    path('search-expenses/',SearchExpenses,name='search-expenses'),
    path('update-expense/<slug>/',UpdateExpenseView.as_view(),name='update-expense'),
    path('delete-expense/<slug>/',DeleteExpenseView.as_view(),name='delete-expense'),
    path('expense-summary-json/',expense_category_summary_json,name='expense-category-summary-json-name'),
    path('expense-category-summary-/',ViewExpenseSummary.as_view(),name='expense-summary'),
    path('search-by-date/',search_by_date,name='search-by-date'),
    path('search-within-date/',search_within_date_range,name='search-within-date'),
    path('export-csv/',export_csv,name='export-csv'),
    path('export-pdf/',export_pdf,name='export-pdf'),
    
    
    path('categories/',ExpenseCategoryView.as_view(),name='expense-categories'),
    path('add-expense-category/',AddExpenseCategoryView.as_view(),name='add-expense-category'),
    path('update-expense-category/<slug>/',UpdateExpenseCategoryView.as_view(),name='update-expense-category'),
    path('delete-expense-category/<slug>/',DeleteExpenseCategoryView.as_view(),name='delete-expense-category'),    
]
