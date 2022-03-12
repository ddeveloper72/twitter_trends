import tweepy
import json
from tweepy import OAuthHandler
from twitter import twitter_api, get_auth

auth = get_auth()

API = tweepy.API(auth)

DUB_WOE_ID = 560743
LON_WOE_ID = 44418
CTN_WOE_ID = 1591691

lon_trends = API.get_place_trends(LON_WOE_ID)
ctn_trends = API.get_place_trends(CTN_WOE_ID)
dub_trends = API.get_place_trends(DUB_WOE_ID)

dub_trends_set = set([trend['name']
                      for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name']
                      for trend in lon_trends[0]['trends']])

ctn_trends_set = set([trend['name']
                      for trend in ctn_trends[0]['trends']])

common_trends = set.intersection(dub_trends_set, lon_trends_set)

print(common_trends)
