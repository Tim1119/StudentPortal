from .models import Profile 
from django import form
from django.core.exceptions import ValidationError
class ProfileForm(form.ModelForm):
    
    class Meta:
        model = Profile 
        fields = ['full_name','company','job','country','address','phone_number','about','twitter','facebook','instagram','linkedin']  
        
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            user_fields = ['full_name','company','job','country','address','phone_number','about','twitter','facebook','instagram','linkedin']  
            for field in user_fields:
                self.fields[field].widget.attrs.update({'class': 'form-control'})
                
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if len(phone_number) > 11:
            raise ValidationError('phone number cannot have more than 11 numbers') 
        return phone_number
        