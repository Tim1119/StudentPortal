from django.shortcuts import render
from django.views.generic import View,TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

class AddExpenseView(TemplateView):
    template_name = 'add-expenses.html'
