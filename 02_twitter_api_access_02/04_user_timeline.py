import tweepy
from tweepy import OAuthHandler

from twitter import twitter_api, get_auth

api = twitter_api()

auth = get_auth()

api = tweepy.API(auth)

user = api.get_user('@DGFalconer')

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a tweet
    print(status.text)
    


