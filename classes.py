import tweepy

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"\nUser: {tweet.user.name} (@{tweet.user.screen_name})\nTweet: {tweet.text}\n\n-------")
        with open('extarcted.cvs','a') as f:
            f.write(f"{tweet.user.screen_name}, {tweet.text}\n")

    def on_error(self, status):
        print("Error detected")