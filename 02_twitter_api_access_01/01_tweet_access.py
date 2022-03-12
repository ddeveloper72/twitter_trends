import tweepy
import json
from tweepy import OAuthHandler
from twitter import twitter_api, get_auth

auth = get_auth()

API = tweepy.API(auth)

count = 10
query = "Dublin"

# Get all status
results = [status for status in tweepy.Cursor(
    API.search_tweets, q=query).items(count)]

for result in results:
    print(json.dumps(result._json, indent=2))
