from django.contrib import admin
from .models import Expense,ExpenseCategory
# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
    

    
    
    list_display = ('owner','amount','category','description','expense_date')
    search_fields = ('amount','description','expense_date')

admin.site.register(Expense,ExpenseAdmin)
admin.site.register(ExpenseCategory)
