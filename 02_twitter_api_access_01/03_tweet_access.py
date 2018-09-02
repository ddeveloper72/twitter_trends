import tweepy
import json
from tweepy import OAuthHandler
from collections import Counter

CONSUMER_KEY = '2qQ4vmRTQQrwBPuwKKT9Z1tK5'
CONSUMER_SECRET = 'eZlUqu2cC4mR0KSH7zyQDoOVKi7G0IjSMZDlK7JrbkNydVtNMW'
OAUTH_TOKEN = '2210195938-I4OI0EzOR7bmBHLv0xNXHaX34ZoK43D4GGxpODH'
OAUTH_TOKEN_SECRET = 'MOLfbCl133CUYo6DscSt5rmxHksRbdQ7k3tfNzlapDISk'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

count = 50
query = "Weather"

# Get all status
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

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

for entry in [screen_names, hashtags, words]:
    counter = Counter(entry)
    print(counter.most_common()[:10]) # the top 10 results


                            
            
