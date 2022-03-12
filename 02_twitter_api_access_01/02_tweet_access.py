import tweepy
import json
from tweepy import OAuthHandler
from twitter import twitter_api, get_auth

auth = get_auth()

API = tweepy.API(auth)

count = 50
query = "Dublin"

# Get all status
results = [status for status in tweepy.Cursor(
    API.search_tweets, q=query).items(count)]

status_texts = [status._json['text'] for status in results]

screen_names = [status._json['user']['screen_name']
                for status in results
                for mention in status._json['entities']['user_mentions']]

hashtags = [hashtag['text']
            for status in results
            for hashtag in status._json['entities']['hashtags']]

words = [word
         for text in status_texts
         for word in text.split()]

print(json.dumps(status_texts[0:5], indent=1))
print(json.dumps(screen_names[0:5], indent=1))
print(json.dumps(hashtags[0:5], indent=1))
print(json.dumps(words[0:5], indent=1))
