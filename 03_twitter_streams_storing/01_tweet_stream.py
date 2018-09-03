from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from twitter import twitter_api, get_auth

api = twitter_api()

keyword_list =['premier league'] # Track list

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
            print("Failed on data: %s"%str(e))
        return True
        
    def on_error(self, status):
        print(status)
        return True
        
auth = get_auth()

twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)



