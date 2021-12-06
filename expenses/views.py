from django.contrib.auth.models import User
from django.http import JsonResponse, request,Http404
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ExpenseCategory, Expense
from django.contrib import messages
from .forms import ExpenseForm,ExpenseCategoryForm
from django.urls import reverse_lazy,reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.decorators.http import require_http_methods
from settings.models import UserPreferences
from django.contrib.auth.decorators import login_required
import datetime,csv,json
# Create your views here.
  
class ExpenseView(LoginRequiredMixin,ListView):
    """This View lists all the expenses a user incures"""
    model = Expense
    template_name = 'expenses.html'
    context_object_name = 'expenses' 
    paginate_by = 5
    
    def get_queryset(self):
        expenses = Expense.objects.filter(owner=self.request.user)
        return expenses 
         

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get currency of user
        currency = UserPreferences.objects.get(user=self.request.user)
        context['currency'] = currency
        
        return context
    
    

class AddExpenseView(LoginRequiredMixin,CreateView):
    """This View helps users to add expense"""
    model = Expense
    form_class = ExpenseForm
    template_name='add-expense.html'
    
    def get_context_data(self, **kwargs):
        context =  super(AddExpenseView,self).get_context_data(**kwargs)
        context['form'].fields['category'].queryset = ExpenseCategory.objects.filter(owner=self.request.user)
        return context
    
   

    
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
            return render(request,'add-expense.html',{'form':form})
        
 
    
    
class UpdateExpenseView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    """This View helps user Update their expenses"""
    model = Expense
    form_class = ExpenseForm
    template_name = 'update-expense.html' 
    success_message = "Expense was updated sucessfully"
    success_url =  reverse_lazy('expenses:expenses') 
    
    def get_context_data(self, **kwargs):
        context =  super(UpdateExpenseView,self).get_context_data(**kwargs)
        context['form'].fields['category'].queryset = ExpenseCategory.objects.filter(owner=self.request.user)
        return context
    
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(UpdateExpenseView, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj

    
   
    
class DeleteExpenseView(LoginRequiredMixin,DeleteView):
    """This view helps users delete expenses"""
    model = Expense
    success_url = reverse_lazy('expenses:expenses') 
    
    def get_success_url(self):
        messages.success(self.request,"Expense was deleted sucessfully")
        return reverse('expenses:expenses') 
    
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(DeleteExpenseView, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj


@login_required
@require_http_methods('POST')
def SearchExpenses(request):
    """This view helps user to search for expense by category"""
    search_str = json.loads(request.body).get('searchText') 
    expensecategory = ExpenseCategory.objects.filter(name__icontains=search_str)
    expenses = Expense.objects.filter(category__in=expensecategory,owner=request.user)
    data = expenses.values()
    return JsonResponse(list(data), safe=False)
    
@login_required
@require_http_methods('POST')   
def expense_category_summary_json(request):
    """Generates expense total amount based on category for expense summary page by default"""
    todays_date = datetime.date.today()
    six_months_ago = todays_date - datetime.timedelta(days=180)
    expenses = Expense.objects.filter(expense_date__gte=six_months_ago,expense_date__lte = todays_date,owner=request.user)
    finalrep = {}
    
    for expense in expenses:
       if  finalrep.get(expense.category.name) is not None:
           finalrep[expense.category.name]+= expense.amount
       else:
           finalrep[expense.category.name] = expense.amount
    return JsonResponse({'expense_category_data':finalrep},safe=False)


class ViewExpenseSummary(LoginRequiredMixin,TemplateView):
    """This is the default view for the expense summary page"""
    template_name = "expense-stats.html" 

@login_required
@require_http_methods('POST') 
def search_by_date(request):
    """This view helps user to search for expense incurred on a specific date"""
    date = json.loads(request.body).get('date')     
    expenses = Expense.objects.filter(expense_date=date,owner=request.user)
    finalrep = {}
    for expense in expenses:
       if  finalrep.get(expense.category.name) is not None:
           finalrep[expense.category.name]+= expense.amount
       else:
           finalrep[expense.category.name] = expense.amount
    return JsonResponse({'expense_category_data':finalrep},safe=False)


@require_http_methods('POST')
def search_within_date_range(request):
    """This view helps users search for expenses incurred with a date range eg from 2/22/2021 to current day"""
    date = json.loads(request.body).get('date')     
    todays_date = todays_date = datetime.date.today()
    expenses = Expense.objects.filter(expense_date__gte=date,expense_date__lte = todays_date,owner=request.user)
    finalrep = {}
    
    for expense in expenses:
       if  finalrep.get(expense.category.name) is not None:
           finalrep[expense.category.name]+= expense.amount
       else:
           finalrep[expense.category.name] = expense.amount
    return JsonResponse({'expense_category_data':finalrep},safe=False)

@login_required
@require_http_methods('GET')
def export_csv(request):
    """This view helps user to export expenses data as csv"""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=expenses'+str(request.user.username)+str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Description','Category','Amount','Date'])
    
    expenses = Expense.objects.filter(owner=request.user)
    
    for expense in expenses:
        writer.writerow([expense.description,expense.category,expense.amount,expense.expense_date])
    return response


@login_required
@require_http_methods('GET')
def export_pdf(request,*args, **kwargs):
    """This view helps users to export expenses data as pdf"""
    expenses = Expense.objects.filter(owner=request.user)
    currency = UserPreferences.objects.get(user=request.user)
    return render(request,'expense-pdf-output.html',context={'expenses':expenses,'currency':currency})



#------------------------------------Income Sources-----------------------------------------------
class ExpenseCategoryView(LoginRequiredMixin,ListView):
    """Lets users view all their income sources"""
    model = ExpenseCategory
    template_name = 'expense-category/expense-category.html' 
    paginate_by = 5
    context_object_name = 'expense_categories' 
    
    def get_queryset(self):
        # Get income  sources queryset
        expense_categories =ExpenseCategory.objects.filter(owner=self.request.user)
        return expense_categories
        
class AddExpenseCategoryView(LoginRequiredMixin,CreateView):
    form_class =ExpenseCategoryForm
    template_name='expense-category/add-expense-category.html'
    
    
   
    
    def post(self,request,*args, **kwargs):
        form =ExpenseCategoryForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            form.save()
            messages.success(request,'Expense category has been added succesfully')
            return redirect('expenses:expense-categories')
        else:
            messages.error(request,'Sorry, your expense category could not be added due to an errror')
            return render(request,'expense-category/add-expense-category.html',{'form':form})
            
            
class UpdateExpenseCategoryView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = ExpenseCategory
    form_class = ExpenseCategoryForm
    template_name = 'expense-category/update-expense-category.html'
    success_message = "Expense category was updated sucessfully"
    success_url =  reverse_lazy('expenses:expense-categories') 
    
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(UpdateExpenseCategoryView, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj
    

class DeleteExpenseCategoryView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model =ExpenseCategory
    success_url = reverse_lazy('expenses:expense-categories') 
    
    def get_success_url(self):
        messages.success(self.request, "Expense category was deleted sucessfully")
        return reverse('expenses:expense-categories')
    
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(DeleteExpenseCategoryView, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj


