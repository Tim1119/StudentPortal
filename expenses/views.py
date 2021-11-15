import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ExpenseCategory, Expense
from django.contrib import messages
from .forms import ExpenseForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.decorators.http import require_http_methods
from settings.models import UserPreferences
# Create your views here.
  
class ExpenseView(LoginRequiredMixin,ListView):
    model = Expense
    template_name = 'expenses.html'
    context_object_name = 'expenses' 
    paginate_by = 5
         

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get currency of user
        currency = UserPreferences.objects.get(user=self.request.user)
        context['currency'] = currency
        # Get all user expenses
        expenses = Expense.objects.filter(owner=self.request.user)
        context['expenses'] = expenses
        return context
    
    

class AddExpenseView(LoginRequiredMixin,CreateView):
    form_class = ExpenseForm
    template_name='add-expense.html'
    
    def post(self,request,*args, **kwargs):
        form = ExpenseForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            form.save()
            messages.success(request,'Expense has been added succesfully')
            return redirect('expenses:expenses')
        else:
            messages.error(request,'Sorry, your expense could not be added due to an errror')
            return redirect('expenses:add-expenses')
            
class UpdateExpenseView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'update-expense.html' 
    success_message = "Expense was updated sucessfully"
    success_url =  reverse_lazy('expenses:expenses') 
    
class DeleteExpenseView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Expense
    success_message = "Expense was deleted sucessfully"
    success_url = reverse_lazy('expenses:expenses') 



@require_http_methods('POST')
def SearchExpenses(request):
    search_str = json.loads(request.body).get('searchText') 
    
    expensecategory = ExpenseCategory.objects.filter(name__icontains=search_str)
    expenses = Expense.objects.filter(category__in=expensecategory,owner=request.user)
    data = expenses.values()
    return JsonResponse(list(data), safe=False)
    
    

    
    