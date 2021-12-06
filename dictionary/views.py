from django.shortcuts import render
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from .forms import DictionaryForm
import requests
from django.http import JsonResponse
import json
from django.views.decorators.http import require_http_methods
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
class DictionaryView(LoginRequiredMixin,View):
    
    def get(self,request,*args, **kwargs):
        form = DictionaryForm()
        return render(request,'dictionary.html',{'form':form})
    
    
@login_required
@require_http_methods('POST')
def SearchDictionaryView(request):
    """Search Dictionary for user data"""
    #search_text = json.loads(request.body).get('search_text')    
    search_text = request.POST.get('search_text') 
    result_list = [] 
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+search_text
    request_result = requests.get(url)
    answer = request_result.json()
    #print(answer)
   
    result_dict = {}
    try:
        phonetics = answer[0]['phonetics'][0]['text']
        audio = answer[0]['phonetics'][0]['audio']
        definition = answer[0]['meanings'][0]['definitions'][0]['definition']
        synonyms = answer[0]['meanings'][0]['definitions'][0]['synonyms']
        
        result_dict = {
            'phonetics':phonetics,
            'audio':audio,
            'definition':definition,
            
            'synonyms':synonyms,
        }
        
    except Exception as e:
        pass
   
    return JsonResponse(result_dict,safe=False)
        