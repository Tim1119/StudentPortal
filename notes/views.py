from django.http.response import Http404
from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView
from django.views.generic.edit import CreateView, DeleteView
from .models import Note,Course
from .forms import NoteForm,CourseForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse,reverse_lazy
from django.views.decorators.http import require_http_methods
import json 
from django.http import JsonResponse


# Create your views here.
class NoteListView(LoginRequiredMixin,ListView):
    model = Note
    template_name= 'notes.html'
    context_object_name = 'all_notes'
    paginate_by = 10

    def get_queryset(self):
        all_notes = Note.objects.filter(profile=self.request.user.profile)
        return all_notes


class NoteDetailView(LoginRequiredMixin,DetailView):
    model = Note
    template_name = 'note-detail.html'
         
    def get_object(self, queryset=None):
        note = super(NoteDetailView,self).get_object()
        if not note.profile == self.request.user.profile:
            raise Http404('<h1>Note owner not found</h1>')
        return note
    
    
    
class NoteEditView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model = Note 
    form_class = NoteForm
    template_name = 'note-edit.html'
    success_url = reverse_lazy('notes:all-notes')
    success_message = 'Note was successfully updated'
    
    def get_object(self, queryset=None):
        note = super(NoteEditView,self).get_object()
        if not note.profile == self.request.user.profile:
            raise Http404('<h1>Note owner not found</h1>')
        return note
    
    

class NoteCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Note 
    form_class = NoteForm
    success_url = reverse_lazy('notes:all-notes')
    success_message = 'Note was successfully Created'
    template_name = 'create-note.html'
    
    def form_valid(self, form):
        self.instance = form.save(commit=False)
        self.instance.profile = self.request.user.profile
        self.instance.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context =  super(NoteCreateView,self).get_context_data(**kwargs)
        context['form'].fields['course'].queryset=Course.objects.filter(owner=self.request.user.profile)
        return context
    

    
class NoteDeleteView(LoginRequiredMixin,DeleteView):
    model = Note
    
    def get_success_url(self):
        messages.success(self.request, "note was deleted sucessfully")
        return reverse('notes:all-notes') 
    
    
    def get_object(self, queryset=None):
        note = super(NoteDeleteView,self).get_object()
        if not note.profile == self.request.user.profile:
            raise Http404('<h1>Note owner not found</h1>')
        return note



@require_http_methods('POST')
def SearchNoteTitle(request):
    search_str = json.loads(request.body).get('searchText') 
    notes = Note.objects.filter(title__icontains=search_str,profile=request.user.profile)
    print(notes)
    data = notes.values()
    return JsonResponse(list(data), safe=False)






#------------------------------------Income Sources-----------------------------------------------
class CourseView(LoginRequiredMixin,ListView):
    """Lets users view all their courses"""
    model = Course
    template_name = 'course-templates/course.html' 
    paginate_by = 5
    context_object_name = 'courses' 
    
    def get_queryset(self):
        # Get income  sources queryset
        courses = Course.objects.filter(owner=self.request.user.profile)
        return courses
        
class  CreateCourseView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    form_class = CourseForm
    success_url = reverse_lazy('notes:all-courses')
    success_message = 'Course was successfully created'
    template_name = 'course-templates/add-course.html' 
    
    
    def form_valid(self, form):
        self.instance = form.save(commit=False)
        self.instance.owner = self.request.user.profile
        self.instance.save()
        return super().form_valid(form)
            
            
class UpdateCourseView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Course
    form_class = CourseForm
    template_name ='course-templates/update-course.html' 
    success_message = "Course was updated successfully"
    success_url =  reverse_lazy('notes:all-courses') 
    
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(UpdateCourseView, self).get_object()
        if not obj.owner == self.request.user.profile:
            raise Http404('<h1>You are not the owner</h1>')
        return obj
    

class DeleteCourseView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Course
   
    def get_success_url(self):
        messages.success(self.request, "Income source was deleted sucessfully")
        return reverse('notes:all_courses')
    
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(DeleteCourseView, self).get_object()
        if not obj.profile == self.request.user.profile:
            raise Http404('<h1>You are not the owner</h1>')
        return obj

