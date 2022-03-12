import tweepy
import json
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from twitter import twitter_api, get_auth

auth = get_auth()

API = tweepy.API(auth)

count = 10
query = "#Dublin"

# Get all status
results = [status for status in tweepy.Cursor(
    api.search_tweets, q=query).items(count)]

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

for lable, data in (('Text', status_texts),
                    ('Screen Name', screen_names),
                    ('Hashtags', hashtags)):
    table = PrettyTable(field_names=[lable, 'Count'])
    counter = Counter(data)
    [table.add_row(entry) for entry in counter.most_common()[:10]]
    # left & right align the columns
    table.align[lable], table.align['Count'] = 'l', 'r'
    print(table)


def get_lexical_diversity(items):
    return 1.0*len(set(items))/len(items)


def get_average_words(tweets):
    total_words = sum([len(tweet.split()) for tweet in tweets])
    return 1.0*total_words/len(tweets)


print("Average Words: {0}".format(get_average_words(status_texts)))
print("Word Diversity: {0}".format(get_lexical_diversity(words)))
print("Screen Name Diversity: {0}".format(get_lexical_diversity(screen_names)))
print("Hashtag Diversity: {0}".format(get_lexical_diversity(hashtags)))
