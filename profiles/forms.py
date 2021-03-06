from .models import Profile 
from django.forms import ModelForm

class ProfileForm(ModelForm):
    
    class Meta:
        model = Profile 
        fields = ['avatar','company','job','country','address','about','twitter','facebook','instagram','linkedin']  
        
        
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['avatar'].widget.attrs.update({'class': 'form-control'})
            self.fields['company'].widget.attrs.update({'class': 'form-control'})
            self.fields['job'].widget.attrs.update({'class': 'form-control'})
            self.fields['country'].widget.attrs.update({'class': 'form-control'})
            self.fields['address'].widget.attrs.update({'class': 'form-control'})
            self.fields['about'].widget.attrs.update({'class': 'form-control'})
            self.fields['twitter'].widget.attrs.update({'class': 'form-control'})
            self.fields['facebook'].widget.attrs.update({'class': 'form-control'})
            self.fields['instagram'].widget.attrs.update({'class': 'form-control'})
            self.fields['linkedin'].widget.attrs.update({'class': 'form-control'})
   
        