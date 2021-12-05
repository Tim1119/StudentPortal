from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from .forms import BookForm
import requests
from django.http import JsonResponse
import json
from django.views.decorators.http import require_http_methods
# Create your views here.
class BookView(View):
    
    def get(self,request,*args, **kwargs):
        form = BookForm()
        return render(request,'book.html',{'form':form})
    
@require_http_methods('POST')
def SearchBookView(request):
    """Search Book for user data"""
    search_text = json.loads(request.body).get('search_text')    
    
    result_list = [] 
    url = "https://www.googleapis.com/books/v1/volumes?q="+search_text
    request_result = requests.get(url)
    answer = request_result.json()
    print(answer)
    for i in range(10):
        result_dict = {
                'title':answer['items'][i]['volumeInfo']['title'],
                'subtitle':answer['items'][i]['volumeInfo'].get('subtitle'),
                'description':answer['items'][i]['volumeInfo'].get('description'),
                'count':answer['items'][i]['volumeInfo'].get('count'),
                'category':answer['items'][i]['volumeInfo'].get('category'),
                'rating':answer['items'][i]['volumeInfo'].get('pageRating'),
                'thumbnail':answer['items'][i]['volumeInfo'].get('imageLinks')['thumbnail'],
                'preview':answer['items'][i]['volumeInfo'].get('previewLink')
            }
       
        result_list.append(result_dict)
        print(result_list)
    return JsonResponse(result_list,safe=False)
        