import json
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Income,Source
from django.contrib import messages
from .forms import IncomeForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.decorators.http import require_http_methods
from settings.models import UserPreferences
# Create your views here.
  
class IncomeView(LoginRequiredMixin,ListView):
    model = Income
    template_name = 'income.html' 
    paginate_by = 5
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get income queryset
        income = Income.objects.filter(owner=self.request.user)
        context['income_sources'] = income 
        # get currency of user
        currency = UserPreferences.objects.get(user=self.request.user)
        context['currency'] = currency
        return context

class AddIncomeView(LoginRequiredMixin,CreateView):
    form_class = IncomeForm
    template_name='add-income.html'
    
    def post(self,request,*args, **kwargs):
        form = IncomeForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            form.save()
            messages.success(request,'Income has been added succesfully')
            return redirect('income:income')
        else:
            messages.error(request,'Sorry, your income could not be added due to an errror')
            return redirect('income:add-income')
            
class UpdateIncomeView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Income
    form_class = IncomeForm
    template_name = 'update-income.html' 
    success_message = "Income was updated sucessfully"
    success_url =  reverse_lazy('income:income') 
    
class DeleteIncomeView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Income
    success_message = "Income was deleted sucessfully"
    success_url = reverse_lazy('income:income') 



@require_http_methods('POST')
def SearchIncome(request):
    search_str = json.loads(request.body).get('searchText') 
    
    money_source = Source.objects.filter(name__icontains=search_str)
    expenses = Income.objects.filter(source__in=money_source,owner=request.user)
    data = expenses.values()
    return JsonResponse(list(data), safe=False)
    