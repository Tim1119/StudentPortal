from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import (
    MinimumLengthValidator,NumericPasswordValidator,CommonPasswordValidator,UserAttributeSimilarityValidator)
from django.contrib.auth.password_validation import validate_password

class  RegisterForm(UserCreationForm):

    email= forms.EmailField(validators=[EmailValidator('email is invalid')],required=True)
    first_name = forms.CharField(max_length=100,required=True)
    last_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model =User
        fields = ['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
            self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
            self.fields['username'].widget.attrs.update({'class': 'form-control'})
            self.fields['password1'].widget.attrs.update({'class': 'form-control'})
            self.fields['password2'].widget.attrs.update({'class': 'form-control'})
            self.fields['email'].widget.attrs.update({'class': 'form-control'})

            for fieldname in ['username','email','password1','password2']:
                self.fields[fieldname].help_text=None
                
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('sorry email is already taken')
        return email

class LoginUserForm(AuthenticationForm):
      
    class Meta:
        model = User 
        fields= ['username','password']

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['username'].widget.attrs.update({'class': 'form-control'})
            self.fields['password'].widget.attrs.update({'class': 'form-control'})
            
class ResetPasswordForm(forms.Form):
    email = forms.EmailField(validators=[EmailValidator(message='your email is invalid')])
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['email'].widget.attrs.update({'class': 'form-control'})

class CompleteResetPasswordForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput())              
    password2 = forms.CharField(widget=forms.PasswordInput())              
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['password1'].widget.attrs.update({'class': 'form-control'})          
            self.fields['password2'].widget.attrs.update({'class': 'form-control'})     
            
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2") 
        
        if password1 != password2:
            raise ValidationError('passwords not matching') 
        
    
    
    def clean_password1(self):
        password1 = self.cleaned_data["password1"]
        if len(password1) < 6:
            raise ValidationError('password1 must be at least six characters long')
        if not str(password1).isalnum():
            raise ValidationError('password1 must be alphanumeric')
        return password1
    
    def clean_password2(self):
        password2 = self.cleaned_data["password2"]
        if len(password2) < 6:
            raise ValidationError('password2 must be at least six characters long')
        if not str(password2).isalnum():
            raise ValidationError('password2 must be alphanumeric')
        return password2
    
            
  