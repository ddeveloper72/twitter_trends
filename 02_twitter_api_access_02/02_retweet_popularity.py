import tweepy
import json
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter
from twitter import twitter_api, get_auth

auth = get_auth()

API = tweepy.API(auth)

count = 10
query = "#allirelandfinal"

# get all tweets for the search query
results = [status for status in tweepy.Cursor(
    API.search_tweets, q=query).items(count)]

min_retweets = 10   # The minimum number of times a status is retweeted to gain
# entry into our list.  We change this to suit our own purposes.

pop_tweets = [status
              for status in results
              if status._json['retweet_count'] > min_retweets]

# Create a list of tweet-tuples, associating each tweet's text with it's tweet count
tweet_tups = [(tweet._json['text'].encode('utf-8'), tweet._json['retweet_count'])
              for tweet in pop_tweets]

# Sort the tuple entries into descending order
most_popular_tups = sorted(tweet_tups, key=itemgetter(1), reverse=True)[:5]

# Pretify the output to console
table = PrettyTable(field_names=['Text', 'Retweet Count'])
for key, val in most_popular_tups:
    table.add_row([key, val])
table.max_width['Text'] = 50
table.align['Text'], table.align['Retweet Count'] = 'l', 'r'  # align columns
print(table)
