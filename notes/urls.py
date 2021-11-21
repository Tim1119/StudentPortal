from django.urls import path
from .views import (
    NoteListView,NoteDeleteView,NoteDetailView,NoteCreateView,NoteEditView
)

app_name = 'notes'

urlpatterns = [

    path('',NoteListView.as_view(),name='all-notes'),
    path('add-note/',NoteCreateView.as_view(),name='create-note'),
    path('note-detail/<slug>',NoteDetailView.as_view(),name='note-detail'),
    path('update-note/<slug>/',NoteEditView.as_view(),name='update-note'),
    path('delete-income/<slug>/',NoteDeleteView.as_view(),name='delete-note'),
    
    #path('export-pdf/',export_pdf,name='export-pdf'),
       
]