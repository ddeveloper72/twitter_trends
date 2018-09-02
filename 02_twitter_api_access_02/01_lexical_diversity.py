import tweepy
import json
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable

CONSUMER_KEY = '2qQ4vmRTQQrwBPuwKKT9Z1tK5'
CONSUMER_SECRET = 'eZlUqu2cC4mR0KSH7zyQDoOVKi7G0IjSMZDlK7JrbkNydVtNMW'
OAUTH_TOKEN = '2210195938-I4OI0EzOR7bmBHLv0xNXHaX34ZoK43D4GGxpODH'
OAUTH_TOKEN_SECRET = 'MOLfbCl133CUYo6DscSt5rmxHksRbdQ7k3tfNzlapDISk'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

count = 10
query = "#Dublin"

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

for lable, data in (('Text', status_texts),
                        ('Screen Name', screen_names),
                        ('Hashtags', hashtags)):
        table = PrettyTable(field_names=[lable, 'Count'])
        counter = Counter(data)
        [table.add_row(entry) for entry in counter.most_common()[:10]]
        table.align[lable], table.align['Count'] = 'l', 'r' # left & right align the columns
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