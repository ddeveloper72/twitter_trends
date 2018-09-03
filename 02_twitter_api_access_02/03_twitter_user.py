import tweepy
from tweepy import OAuthHandler

from twitter import twitter_api, get_auth

api = twitter_api()

auth = get_auth()

api = tweepy.API(auth)

user = api.get_user('@DGFalconer')

print(user.screen_name)
print(user.followers_count)

for friend in user.friends():
    print(friend.screen_name)
    print(friend.followers_count)
    


