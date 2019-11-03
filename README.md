# How Python Talks to Data in...
# Data Centric Development


Welcome to my Python project on Cloud9 IDE!  Yes I've taken over the default Readme
to add in a few more bits about what this [Code Institute](https://courses.codeinstitute.net/) tutorial was all about.

This tutorial focused on creating python apps which tap into the power of the twitter API using [Tweepy](http://www.tweepy.org/)

The Learning Outcomes Are:

1 The Twitter API Intro

   * Register this app with [Twitter Developer](https://developer.twitter.com), 
   * See What's trending, 
   * Look at what's trending in multiple locations
    
2 Twitter API Access

   * Harvest tweets, 
   * Format a tweet, 
   * Access tweet attributes, 
   * Harvest tweet attributes, 
   * Frequency analysis and 
   * Prettify the output.

3 Twitter Streams - Storing Data

   * Access and store the Twitter stream, 
   * Read back the stored data file
    
4 An Introduction to Data Mining!

   * [IPython](https://ipython.org/)
   * [Jupyter](http://jupyter.org/) Notebooks
   * [matplotlib](https://matplotlib.org/)

## The Results!

The charts below were created using Jupyter Notebook:

The app was run from Cloud9

```
keyword_list =['Python', 'JavaScript', 'C#', 'PHP'] # Track list
```

The sample data came from a snapshot of 500 tweets taken and recorded to a json file.

![Language Trends](https://github.com/ddeveloper72/twitter_trends/blob/master/images/twitterBarCharts.PNG "Fig 1 showing Spoken Language Trends")

![Programming Language Trends](https://github.com/ddeveloper72/twitter_trends/blob/master/images/twitterPieCharts.PNG "Fig 2 showing Programming Language Trends")

## Programming Language Trends. 
(Code Sample from the Tutorial, written in Jupyter Notebook)

### 1 Loading our tweets data created from our snapshot

```python
%matplotlib notebook
import matplotlib.pyplot as plt
import json

TWEETS_DATA_PATH = '03_twitter_streams_storing/tweet_mining.json'

def read_json(file_path):
    results = []
    with open(TWEETS_DATA_PATH) as tweets_file:
        for tweet_line in tweets_file:
            try:
                status = json.loads(tweet_line)
                results.append(status)
            except ValueError:
                pass
        return results
```

### 2 Searching the data for keywords- Tokens

```python
import re

def is_token_in_tweet_text(token, tweet_text):
    token = token.lower()
    tweet_text = ''.join(tweet_text).lower()
    match = re.search(token, tweet_text)
    if match:
        return True
    return False

results  = read_json(TWEETS_DATA_PATH)
```

### 3 Counting and categorizing the Keywords

```python
import pandas

statuses = pandas.DataFrame()

statuses['text'] = [status['text'] for status in results]

statuses['python'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('python', status))
statuses['javascript'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('javascript', status))
statuses['c'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('c ', status))
statuses['php'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('php', status))


# Output the number of tweets where it is true that they contain our keywords
print(statuses['python'].value_counts()[True])
print(statuses['javascript'].value_counts()[True])
print(statuses['c'].value_counts()[True])
print(statuses['php'].value_counts()[True])
```

### 4 Charting the Keywords as a Pie Chart

```python
def lang_pie():
    slices = [statuses['python'].value_counts()[True],
             statuses['javascript'].value_counts()[True],
             statuses['c'].value_counts()[True],
             statuses['php'].value_counts()[True]]
    activities = ['Python', 'JavaScript', 'C#', 'PHP']
    cols = ['c', 'm', 'r', 'b']
    
    plt.pie(slices, colors = cols, labels = activities,
           startangle = 90, shadow = True, explode = (0.2, 0, 0.2, 0),
           autopct = '%1.1f%%')
    
    plt.title('Tweet Incidence\n Coding Languages')
    plt.show()
    
lang_pie()
```
