import tweepy
import json
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from twitter import twitter_api, get_auth

auth = get_auth()

API = tweepy.API(auth)

count = 50
query = "Weather"

# Get all status
results = [status for status in tweepy.Cursor(API.search, q=query).items(count)]

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
                        ('Word', words)):
        table = PrettyTable(field_names=[lable, 'Count'])
        counter = Counter(data)
        [table.add_row(entry) for entry in counter.most_common()[:10]]
        table.align[lable], table.align['Count'] = 'l', 'r' # left & right align the columns
        print(table)
                        


                            
            
