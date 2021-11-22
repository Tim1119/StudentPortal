from django.http.response import Http404
from django.views.generic import ListView,DetailView,UpdateView
from django.views.generic.edit import CreateView, DeleteView
from .models import Todo
from .forms import TodoForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse,reverse_lazy
from django.shortcuts import get_object_or_404, redirect,render
from django.views.decorators.http import require_http_methods



# Create your views here.
class TodoListView(LoginRequiredMixin,ListView):
    model = Todo
    template_name= 'todo.html'
    context_object_name = 'all_todos'
    paginate_by = 10

    def get_queryset(self):
        all_todos = Todo.objects.filter(owner=self.request.user.profile)
        return all_todos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = TodoForm()
        context['form'] = form
        return context

 
def TodoEditView(request,slug,*args, **kwargs):
    todo_item = Todo.objects.get(slug=str(slug),owner=request.user.profile)
    form = TodoForm(instance=todo_item)
    if request.method == 'POST':
        form = TodoForm(request.POST or None,instance=todo_item)
        if form.is_valid():
            form.save()
            messages.success(request,'todo item was successfully updated')
            return redirect('todo:all-todos')
        else:
            messages.error(request,'sorry, an error occured your todo item was not update')
            return render(request,'todo-edit.html',{'form':form})
    else:
        return render(request,'todo-edit.html',{'form':form,'todo':todo_item})
            
    

    

class TodoCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo:all-todos')
    success_message = 'Todo-Item was successfully created'
    template_name = 'create-todo.html'
    
    def form_valid(self, form):
        self.instance = form.save(commit=False)
        self.instance.owner = self.request.user.profile
        self.instance.save()
        return super().form_valid(form)
    
    
@require_http_methods('POST')
def TodoDeleteView(request,slug,*args, **kwargs):
    todo_item = Todo.objects.get(slug=str(slug),owner=request.user.profile)
    messages.success(request, "todo was deleted sucessfully")
    todo_item.delete()
    return redirect('todo:all-todos')


@require_http_methods('POST')
def TodoUpdateView(request,slug,*args, **kwargs):
    """Helps user check for completed or non completed task"""
    todo_item = Todo.objects.get(slug=str(slug),owner=request.user.profile)
    if todo_item.completed == True:
        todo_item.completed = False 
        todo_item.save()
    else:
        todo_item.completed = True
        todo_item.save()
    return redirect('todo:all-todos')