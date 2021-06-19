from django.db.models.fields import TextField
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Tweet
# Create your views here.

def home(request, *args, **kwargs):
    return HttpResponse("hello people")

def tweet_list(request, *args, **kwargs):
    tweets = Tweet.objects.all()
    tweet_all = [{'id': tweet.id, 'content':tweet.text} for tweet in tweets]
    data = {
        'response':tweet_all
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


