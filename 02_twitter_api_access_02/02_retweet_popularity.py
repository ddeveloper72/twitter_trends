import tweepy
import json
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter

CONSUMER_KEY = '2qQ4vmRTQQrwBPuwKKT9Z1tK5'
CONSUMER_SECRET = 'eZlUqu2cC4mR0KSH7zyQDoOVKi7G0IjSMZDlK7JrbkNydVtNMW'
OAUTH_TOKEN = '2210195938-I4OI0EzOR7bmBHLv0xNXHaX34ZoK43D4GGxpODH'
OAUTH_TOKEN_SECRET = 'MOLfbCl133CUYo6DscSt5rmxHksRbdQ7k3tfNzlapDISk'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

count = 10
query = "#allirelandfinal"

# get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

min_retweets = 10   # The minimum number of times a status is retweeted to gain
                    # entry into our list.  We change this to suit our own purposes.

pop_tweets = [status
                for status in results
                    if status._json['retweet_count'] > min_retweets]

# Create a list of tweet-tuples, associating each tweet's text with it's tweet count
tweet_tups = [(tweet._json['text'].encode('utf-8'),tweet._json['retweet_count'])
                for tweet in pop_tweets]

# Sort the tuple entries into descending order
most_popular_tups = sorted(tweet_tups, key=itemgetter(1), reverse=True)[:5]

# Pretify the output to console
table = PrettyTable(field_names=['Text', 'Retweet Count'])
for key, val in most_popular_tups:
    table.add_row([key, val])
table.max_width['Text']=50
table.align['Text'],table.align['Retweet Count']= 'l', 'r' # align columns
print(table)