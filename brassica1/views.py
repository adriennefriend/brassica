from django.shortcuts import render
from django.conf import settings
import requests
import tweepy
import wikipedia
import time

def index(request):
    start = current_milli_time()
    print 'START: ', start
    
    auth = tweepy.OAuthHandler(
        settings.TWITTER_CONSUMER_KEY,
        settings.TWITTER_CONSUMER_SECRET
    )
    auth.set_access_token(
        settings.TWITTER_ACCESS_TOKEN,
        settings.TWITTER_ACCESS_SECRET_TOKEN
    )
    twitter = tweepy.API(auth)

    if 'query' in request.GET:
        query = request.GET['query']
        
        twitterdata = twitter.search(query, 'en')
        print 'AFTER TWITTER CALL: ', current_milli_time() - start
        wikidata = wikipedia.search(query)
        print 'AFTER WIKIPEDIA CALL: ', current_milli_time() - start
    else: 
        twitterdata = None
        wikidata = None
    
    
    return render(request, 'index.html', {'twitter': twitterdata, 'wikipedia': wikidata
        })
        
def current_milli_time():
    return int(round(time.time() * 1000)) # to get the current time in miliseconds

