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

dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)

dub_trends_set = set([trend['name']
                    for trend in dub_trends[0]['trends']])
                    
lon_trends_set = set([trend['name']
                    for trend in lon_trends[0]['trends']])
                    
common_trends = set.intersection(dub_trends_set, lon_trends_set)

print(common_trends)