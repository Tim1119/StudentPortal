from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from .forms import WikipediaForm
import requests
from django.http import JsonResponse
import json
from django.views.decorators.http import require_http_methods
import wikipedia
# Create your views here.
class WikipediaView(View):
    
    def get(self,request,*args, **kwargs):
        form = WikipediaForm()
        return render(request,'wikipedia.html',{'form':form})
    
@require_http_methods('POST')
def SearchWikipediaView(request):
    """Search Wikipedia for user data"""
    
    search_text = request.POST.get('search_text') 
    wiki_search = wikipedia.page(search_text)
    print(wiki_search)
    result_dict ={
        'title':wiki_search.title,
        'link':wiki_search.url,
        'details':wiki_search.content,
        'summary':wiki_search.summary
        }
    result_list = [] 
    result_list.append(result_dict)
    return JsonResponse(result_list,safe=False)
        