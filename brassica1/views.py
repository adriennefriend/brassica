from django.shortcuts import render
from django.conf import settings
import requests
import tweepy

def index(request):
    auth = tweepy.OAuthHandler(
        settings.TWITTER_CONSUMER_KEY,
        settings.TWITTER_CONSUMER_SECRET
    )
    auth.set_access_token(
        settings.TWITTER_ACCESS_TOKEN,
        settings.TWITTER_ACCESS_SECRET_TOKEN
    )
    api = tweepy.API(auth)

    data = api.search('cookies')
    return render(request, 'index.html', {'twitter': data
        })
        



# in the controller, there's a function for each endpoint
# one controller and maybe two methods maybe one
# views.py, where we are now, is where the controller is
# controllers are in views.py
# views are in template (index.html)
# at the end of a controller, you'll call render, pass the request, and the view that you want to display, and then a list a variables to pass to the view. we're passing the data variable to the view. 

# decided to use tweepy for Twitter since it is a pain
# added the tokens here because we couldn't think where else to add them
# want to make settings.py part of gitignore
