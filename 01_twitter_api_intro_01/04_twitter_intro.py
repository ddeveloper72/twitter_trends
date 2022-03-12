import tweepy
import json
from tweepy import OAuthHandler
from twitter import twitter_api, get_auth

auth = get_auth()

API = tweepy.API(auth)

DUB_WOE_ID = 560743
LON_WOE_ID = 44418
ORK_WOE_ID = 560472
SNN_WOE_ID = 560472
GWY_WOE_ID = 560912

dub_trends = API.get_place_trends(DUB_WOE_ID)
snn_trends = API.get_place_trends(SNN_WOE_ID)
ork_trends = API.get_place_trends(ORK_WOE_ID)
gwy_trends = API.get_place_trends(GWY_WOE_ID)


dub_trends_set = set([trend['name']
                      for trend in dub_trends[0]['trends']])

snn_trends_set = set([trend['name']
                      for trend in snn_trends[0]['trends']])

ork_trends_set = set([trend['name']
                      for trend in ork_trends[0]['trends']])

gwy_trends_set = set([trend['name']
                      for trend in gwy_trends[0]['trends']])

common_trends = set.intersection(
    dub_trends_set, ork_trends_set, gwy_trends_set)

print(common_trends)
