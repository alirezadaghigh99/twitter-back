from typing import NewType
from django.db.models.fields import TextField
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import Tweet
# Create your views here.

def home(request, *args, **kwargs):
    return HttpResponse("hello people")

def tweet_create(request, *args, **kwargs):
    data = request.POST or None
    print('received data is ', data)
    content = data['content']
    next_url = data['next']
    new_tweet = Tweet.objects.create(text=content)
    new_tweet.save()
    return redirect(next_url)



def tweet_list(request, *args, **kwargs):
    tweets = Tweet.objects.all()
    tweet_all = [{'id': tweet.id, 'content':tweet.text, 'likes':35} for tweet in tweets]
    data = {
        'isUser':False,
        'response':tweet_all,
        
    }
    return JsonResponse(data=data)

def tweet_detail(request, *args, **kwargs):
    id_ = int(kwargs.get('tweet_id'))
    data = {
        'id' :id_, 
    }
    try:
        tweet = Tweet.objects.get(id=id_)
        data['content'] = tweet.text
    except:
        data["message"] = "tweet not found"

    return JsonResponse(data, status= 404)


