import tweepy

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"\nUser: {tweet.user.name} (@{tweet.user.screen_name})\nTweet: {tweet.text}\n\n-------")
        if "RT @" in tweet.text:
            print('retweeted')
        
    def on_error(self, status):
        print("Error detected")