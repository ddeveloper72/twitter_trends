import tweepy
import json
from tweepy import OAuthHandler
from twitter import twitter_api, get_auth

api = twitter_api()

auth = get_auth()

api = tweepy.API(auth)

count = 10
query = "Dublin"

# Get all status
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

for result in results:
    print (json.dumps(result._json, indent=2))