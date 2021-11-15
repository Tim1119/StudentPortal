from django.shortcuts import render
import os 
import json 
from django.conf import settings
from django.views.decorators.http import require_POST
from .models import UserPreferences
from django.http import JsonResponse



# Create your views here.
def settingsView(request):
    user_preferences= UserPreferences.objects.get(user=request.user)
    currency_data = [] 
    file_path = os.path.join(settings.BASE_DIR,'currencies.json')
    
    with open(file_path,'r') as json_file:
        data = json.load(json_file)
        
        for key,value in data.items():
            currency_data.append({'name':key,'value':value})
        
    context = {'currencies':currency_data,'user_preferences':user_preferences}
    return render(request,'settings.html',context)

@require_POST
def saveUserSettings(request):
    currency = request.POST.get('currency')
    current_user = request.user
    user_preferences,created = UserPreferences.objects.get_or_create(user=current_user)
    user_preferences.currency  = currency 
    user_preferences.save()
    return JsonResponse({'message':'Your settings has been saved'})
    
    