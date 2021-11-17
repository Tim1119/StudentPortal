class ProfileForm(ModelForm):
    
    class Meta:
        model = Profile 
        fields = ['avatar','company','job','country','address','about','twitter','facebook','instagram','linkedin']  
        
        def __init__(self, *args, **kwargs):
            super(ProfileForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'


            self.fields['job'].widget.attrs.update({'class': 'form-control'})
            self.fields['country'].widget.attrs.update({'class': 'form-control'})
            self.fields['address'].widget.attrs.update({'class': 'form-control'})
            self.fields['about'].widget.attrs.update({'class': 'form-control'})
            self.fields['twitter'].widget.attrs.update({'class': 'form-control'})
            self.fields['facebook'].widget.attrs.update({'class': 'form-control'})
            self.fields['instagram'].widget.attrs.update({'class': 'form-control'})
            self.fields['linkedin'].widget.attrs.update({'class': 'form-control'})

,'job','country','address','about','twitter','facebook','instagram','linkedin'