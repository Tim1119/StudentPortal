from django.forms import ModelForm, forms
from .models import Income,Source

class IncomeForm(ModelForm):
    

    class Meta:
        model = Income
        fields = ['description','amount','income_date','source']
        
        
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            
            self.fields['description'].widget.attrs.update({'class': 'form-control'})
            self.fields['amount'].widget.attrs.update({'class': 'form-control'})
            self.fields['source'].widget.attrs.update({'class': 'form-control'})
            self.fields['income_date'].widget.attrs.update({'class': 'form-control'})
            
class SourceForm(ModelForm):
    
    class Meta:
        model=Source 
        fields = ['name']
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].widget.attrs.update({'class': 'form-control'})