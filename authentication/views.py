from django.shortcuts import render
from django.views.generic import TemplateView,View
import json
from django.http import JsonResponse

# Create your views here.
class RegistrationView(TemplateView):
    template_name = 'registration/register.html'

class UserNameValidationView(View):

    def post(self,request,*args, **kwargs):
        data = json.loads(self.request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'username error':'username should contain alphanumeric characters'})
        else:
            return JsonResponse('username valid',True)




class LoginView(TemplateView):
    template_name = 'registration/login.html'