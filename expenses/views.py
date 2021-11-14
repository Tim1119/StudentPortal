from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
# Create your views here.
  
class AddExpenseView(TemplateView):
    template_name = 'add-expense.html'
