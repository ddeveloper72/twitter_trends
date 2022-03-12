import tweepy
import json
from tweepy import OAuthHandler
from twitter import twitter_api, get_auth

auth = get_auth()

API = tweepy.API(auth)

DUB_WOE_ID = 560743

dub_trends = API.get_place_trends(DUB_WOE_ID)

print(json.dumps(dub_trends, indent=1))
