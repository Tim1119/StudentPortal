import json
from django.http import JsonResponse
from django.http.response import Http404
from django.shortcuts import redirect,render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Income,Source
from django.contrib import messages
from .forms import IncomeForm,SourceForm
from django.urls import reverse_lazy,reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.decorators.http import require_http_methods
from settings.models import UserPreferences
import datetime,csv 
from django.http import HttpResponse

# Create your views here.
  
class IncomeView(LoginRequiredMixin,ListView):
    model = Income
    template_name = 'income.html' 
    paginate_by = 5
    context_object_name = 'income_sources' 
    
    def get_queryset(self):
        # Get income queryset
        income = Income.objects.filter(owner=self.request.user)
        return income
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get currency of user
        currency = UserPreferences.objects.get(user=self.request.user)
        context['currency'] = currency
        return context

class AddIncomeView(LoginRequiredMixin,CreateView):
    model = Income
    form_class = IncomeForm
    template_name='add-income.html'
    
    def get_context_data(self, **kwargs):
        context =  super(AddIncomeView,self).get_context_data(**kwargs)
        context['form'].fields['source'].queryset = Source.objects.filter(owner=self.request.user)
        return context
  
    
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
            return render(request,'add-income.html',{'form':form})
            
            
class UpdateIncomeView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Income
    form_class = IncomeForm
    template_name = 'update-income.html' 
    success_message = "Income was updated sucessfully"
    success_url =  reverse_lazy('income:income') 
    
    def get_context_data(self, **kwargs):
        context =  super(UpdateIncomeView,self).get_context_data(**kwargs)
        context['form'].fields['source'].queryset = Source.objects.filter(owner=self.request.user)
        return context
    
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(UpdateIncomeView, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj
    
   
   
    
class DeleteIncomeView(LoginRequiredMixin,DeleteView):
    model = Income
    success_url = reverse_lazy('income:income') 
    
    def get_success_url(self):
        messages.success(self.request, "Income source was deleted sucessfully")
        return reverse('income:income') 
    
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(DeleteIncomeView, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj



@require_http_methods('POST')
def SearchIncome(request):
    search_str = json.loads(request.body).get('searchText') 
    money_source = Source.objects.filter(name__icontains=search_str)
    expenses = Income.objects.filter(source__in=money_source,owner=request.user)
    data = expenses.values()
    return JsonResponse(list(data), safe=False)

@require_http_methods('POST')
def income_source_summary_json(request):
    """Generates income total amount based on sorces"""
    todays_date = datetime.date.today()
    six_months_ago = todays_date - datetime.timedelta(days=180)
    all_income = Income.objects.filter(income_date__gte=six_months_ago,income_date__lte = todays_date,owner=request.user)
    finalrep = {}
    
    for i in all_income:
       if  finalrep.get(i.source.name) is not None:
           finalrep[i.source.name]+= i.amount
       else:
           finalrep[i.source.name] = i.amount
    return JsonResponse({'income_source_data':finalrep},safe=False)


class ViewIncomeSummary(TemplateView):
    """This is the deault view to view all income chats summary"""
    template_name = "income-stats.html"



@require_http_methods('POST') 
def search_by_date(request):
    """This view helps user to search for expense incurred on a specific date"""
    date = json.loads(request.body).get('date')     
    all_income = Income.objects.filter(income_date=date,owner=request.user)
    finalrep = {}
    for income in all_income:
       if  finalrep.get(income.source.name) is not None:
           finalrep[income.source.name]+= income.amount
       else:
           finalrep[income.source.name] = income.amount
    return JsonResponse({'income_source_data':finalrep},safe=False)


@require_http_methods('POST')
def search_within_date_range(request):
    """This view helps users search for expenses incurred with a date range eg from 2/22/2021 to current day"""
    date = json.loads(request.body).get('date')     
    todays_date = datetime.date.today()
    all_income = Income.objects.filter(income_date__gte=date,income_date__lte = todays_date,owner=request.user)
    finalrep = {}
    
    for income in all_income:
       if  finalrep.get(income.source.name) is not None:
           finalrep[income.sources.name]+= income.amount
       else:
           finalrep[income.source.name] = income.amount
    return JsonResponse({'income_source_data':finalrep},safe=False)

@require_http_methods('GET')
def export_csv(request):
    """This view helps user to export expenses data as csv"""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=income'+str(request.user.username)+str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Description','Category','Amount','Date'])
    
    all_income = Income.objects.filter(owner=request.user)
    
    for income in all_income:
        writer.writerow([income.description,income.source,income.amount,income.income_date])
    return response


@require_http_methods('GET')
def export_pdf(request,*args, **kwargs):
    """This view helps users to export eincome data as pdf"""
    all_income = Income.objects.filter(owner=request.user)
    currency = UserPreferences.objects.get(user=request.user)
    return render(request,'income-pdf-output.html',context={'all_income':all_income,'currency':currency})







#------------------------------------Income Sources-----------------------------------------------
class IncomeSourceView(LoginRequiredMixin,ListView):
    """Lets users view all their income sources"""
    model = Source
    template_name = 'income-sources/source.html' 
    paginate_by = 5
    context_object_name = 'income_sources' 
    
    def get_queryset(self):
        # Get income  sources queryset
        income = Source.objects.filter(owner=self.request.user)
        return income
        
class AddIncomeSourceView(LoginRequiredMixin,CreateView):
    form_class = SourceForm
    template_name='income-sources/add-income-source.html'
    
    def post(self,request,*args, **kwargs):
        form = SourceForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            form.save()
            messages.success(request,'Income source has been added succesfully')
            return redirect('income:sources')
        else:
            messages.error(request,'Sorry, your income source could not be added due to an errror')
            return render(request,'income-sources/add-income-source.html',{'form':form})
            
            
class UpdateIncomeSourceView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Source
    form_class = SourceForm
    template_name = 'income-sources/update-income-sources.html' 
    success_message = "Income source was updated sucessfully"
    success_url =  reverse_lazy('income:sources') 
    
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(UpdateIncomeSourceView, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj
    

class DeleteIncomeSourceView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Source
    success_url = reverse_lazy('income:sources') 
    
    def get_success_url(self):
        messages.success(self.request, "Income source was deleted sucessfully")
        return reverse('income:sources')
    
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(DeleteIncomeSourceView, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj
