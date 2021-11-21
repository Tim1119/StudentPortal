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
