from django.contrib import admin
from django.urls import path, include
from .views import tweet_detail, tweet_list

urlpatterns = [
    path('detail_list/<int:tweet_id>', tweet_detail),
    path("all_tweets/", tweet_list)
]