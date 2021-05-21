import tweepy

auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

APITW = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
