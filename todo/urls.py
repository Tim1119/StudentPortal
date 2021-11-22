from django.urls import path
from .views import TodoListView,TodoCreateView,TodoUpdateView,TodoDeleteView,TodoEditView

app_name = 'todo'

urlpatterns = [
    
    path('all-todo/',TodoListView.as_view(),name='all-todos'),
    path('create-todo/',TodoCreateView.as_view(),name='create-todo'),
    path('edit-todo/<slug>/',TodoEditView,name='edit-todo'),
    path('update-todo/<slug>/',TodoUpdateView,name='update-todo'),
    path('delete-todo/<slug>/',TodoDeleteView,name='delete-todo'),
    
]