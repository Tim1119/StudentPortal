from django.forms import ModelForm 
from .models import Course, Note

class NoteForm(ModelForm):

    class Meta:
        model = Note
        fields = ['title','description','course','note_order','content']
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['title'].widget.attrs.update({'class': 'form-control'})
            self.fields['description'].widget.attrs.update({'class': 'form-control'})
            self.fields['course'].widget.attrs.update({'class': 'form-control'})
            self.fields['note_order'].widget.attrs.update({'class': 'form-control'})
            self.fields['content'].widget.attrs.update({'class': 'form-control'})
         
class CourseForm(ModelForm):
    
    class Meta:
        model = Course
        fields = ['name']
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].widget.attrs.update({'class': 'form-control'})