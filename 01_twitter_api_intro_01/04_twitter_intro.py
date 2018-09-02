import tweepy
import json
from tweepy import OAuthHandler

CONSUMER_KEY = '2qQ4vmRTQQrwBPuwKKT9Z1tK5'
CONSUMER_SECRET = 'eZlUqu2cC4mR0KSH7zyQDoOVKi7G0IjSMZDlK7JrbkNydVtNMW'
OAUTH_TOKEN = '2210195938-I4OI0EzOR7bmBHLv0xNXHaX34ZoK43D4GGxpODH'
OAUTH_TOKEN_SECRET = 'MOLfbCl133CUYo6DscSt5rmxHksRbdQ7k3tfNzlapDISk'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

DUB_WOE_ID = 560743
LON_WOE_ID = 44418
ORK_WOE_ID = 560472
SNN_WOE_ID = 560472
GWY_WOE_ID = 560912

dub_trends = api.trends_place(DUB_WOE_ID)
snn_trends = api.trends_place(SNN_WOE_ID)
ork_trends = api.trends_place(ORK_WOE_ID)
gwy_trends = api.trends_place(GWY_WOE_ID)



dub_trends_set = set([trend['name']
                    for trend in dub_trends[0]['trends']])
                    
snn_trends_set = set([trend['name']
                    for trend in snn_trends[0]['trends']])
                    
ork_trends_set = set([trend['name']
                    for trend in ork_trends[0]['trends']])
                    
gwy_trends_set = set([trend['name']
                    for trend in gwy_trends[0]['trends']])
                    
common_trends = set.intersection(dub_trends_set, ork_trends_set, gwy_trends_set)

print(common_trends)