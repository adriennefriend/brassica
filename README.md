# brassica

Brassica is small Django app that allows a user to enter a term and receive results from Twitter and Wikipedia.

If the page is refreshed, the results will be also.

I used Tracy Osborn's book "Hello Web App" for basic starting structure, and a bit of Bootstrap to make a placeholder for the search bar. Next I tackled learning about APIs, reading the official docs at Twitter and Wikipedia. After registering my app with Twitter, I decided to use Tweepy, an easy-to-use Python library for accessing the API, since it gracefully handles OAUTH. Wikipedia was much more straightforward, especially when using the Wikipedia API for Python.

For profiling, I investigated hotshot and silk, but neither seemed appropriate for my simple project. Instead, I have a function that prints the current time when the application starts, after the Twitter call, and then after the Wikipedia call. 
