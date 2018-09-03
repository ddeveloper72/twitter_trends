import tweepy
import json
from tweepy import OAuthHandler
from twitter import twitter_api, get_auth

api = twitter_api()

auth = get_auth()

api = tweepy.API(auth)

DUB_WOE_ID = 560743

dub_trends = api.trends_place(DUB_WOE_ID)

print(json.dumps(dub_trends, indent=1))