from django.urls import path
from .views import (
    NoteListView,NoteDeleteView,NoteDetailView,NoteCreateView,NoteEditView, SearchNoteTitle,
    SearchNoteTitle, CourseView,CreateCourseView,UpdateCourseView,DeleteCourseView
    
)

app_name = 'notes'

urlpatterns = [

    path('',NoteListView.as_view(),name='all-notes'),
    path('add-note/',NoteCreateView.as_view(),name='create-note'),
    path('note-detail/<slug>',NoteDetailView.as_view(),name='note-detail'),
    path('update-note/<slug>/',NoteEditView.as_view(),name='update-note'),
    path('delete-income/<slug>/',NoteDeleteView.as_view(),name='delete-note'),
    path('search-note-title/',SearchNoteTitle,name='search-note-title'),
       

    path('course/',CourseView.as_view(),name='all-courses'),
    path('create-course/',CreateCourseView.as_view(),name='create-course'),
    path('update-course/<slug>/',UpdateCourseView.as_view(),name='update-course'),
    path('delete-course/<slug>/',DeleteCourseView.as_view(),name='delete-course'),
]