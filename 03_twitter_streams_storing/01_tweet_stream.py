import tweepy
from tweepy import OAuthHandler
from tweepy import StreamListener
from decouple import config


# get secret keys for .env file managed by decouple
CONSUMER_KEY = config('Consumer_Key', default='')
CONSUMER_SECRET = config('Consumer_Secret', default='')
OAUTH_TOKEN = config('OAUTH_Token', default='')
OAUTH_TOKEN_SECRET = config('OAUTH_Token_Secret', default='')

# prep auth for API StreamListener
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# rate limit the number of tweets from the API
api = tweepy.API(auth, wait_on_rate_limit=True)


#  Use a list of keywords to search tweets
keyword_list = ['python', 'javascript', 'php', 'c#']  # Track list

# Write twitter stream to json file.  Exit the write using Ctrl+c on the CLI
class MyStreamListener(StreamListener):

    def __init__(self):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0

    def on_data(self, data):
        try:
            with open('tweet_mining.json', 'a') as tweet_file:
                tweet_file.write(data)
                return True
        except BaseException as e:
            print("Failed on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


twitter_stream = tweepy.Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)
