from django.forms import ModelForm
from .models import Expense,ExpenseCategory 

class ExpenseForm(ModelForm):
    

    class Meta:
        model = Expense
        fields = ['description','amount','expense_date','category']
        
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['description'].widget.attrs.update({'class': 'form-control'})
            self.fields['amount'].widget.attrs.update({'class': 'form-control'})
            self.fields['category'].widget.attrs.update({'class': 'form-control'})
            self.fields['expense_date'].widget.attrs.update({'class': 'form-control'})
            
