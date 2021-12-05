from django import forms 

class DictionaryForm(forms.Form):
    search = forms.CharField(max_length=100)
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['search'].widget.attrs.update({'class': 'form-control'})