from django.forms import ModelForm 
from .models import Todo

class TodoForm(ModelForm):
    
    class Meta:
        model = Todo
        fields = ['task','completed']
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['task'].widget.attrs.update({'class': 'form-control'})
            #self.fields['completed'].widget.attrs.update({'class': 'form-control'})