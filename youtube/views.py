from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from .forms import YoutubeForm
from youtubesearchpython import VideosSearch
from django.http import JsonResponse
import json
from django.views.decorators.http import require_http_methods
# Create your views here.
class YoutubeView(View):
    
    def get(self,request,*args, **kwargs):
        form = YoutubeForm()
        return render(request,'youtube.html',{'form':form})
    
@require_http_methods('POST')
def SearchYoutubeView(request):
    """Search Youtuube for user data"""
    #search_text = json.loads(request.body).get('search_text')    
    search_text = request.POST.get('search_text')
    
    result_list = [] 
    video = VideosSearch(search_text,limit=15)
    for i in video.result()['result']:
        result_dict = {
                'title':i['title'],
                'duration':i['duration'],
                'thumbnail':i['thumbnails'][0]['url'],
                'channel':i['channel']['name'],
                'views':i['viewCount']['text'],
                'link':i['link'],
                'published':i['publishedTime']
            }
        description = ''
        if i['descriptionSnippet']:
            for j in i['descriptionSnippet']:
                    description += j['text']
        result_dict['description'] = description 
        result_list.append(result_dict)
    return JsonResponse(result_list,safe=False)
        