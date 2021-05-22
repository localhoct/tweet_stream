import tweepy
from auth import APITW
from classes import MyStreamListener
import sys

try:
    user_info = APITW.verify_credentials()
    if user_info:
        print("Authentication OK")
        name = user_info._json['name']
        user_name = user_info._json['screen_name']
        user_id = user_info._json['id_str']
        followers = user_info._json['followers_count']
        followings = user_info._json['friends_count']
        joined = user_info._json['created_at']
        tweet_count = user_info._json['statuses_count']
        print(f"Name:{name} \nUserName: {user_name} \nID: {user_id}\nFollowers: {followers} Following: {followings} \nJoined: {joined} \nTweet Count: {tweet_count}")
    else:
        sys.exit(1)

except:
    print("Error during authentication, Please Check your keys!!")
    sys.exit(1)

track_for = input("Please Eenter the hashtag to stream (ex: #python): ")

tweets_listener = MyStreamListener(APITW)
stream = tweepy.Stream(APITW.auth, tweets_listener)
stream.filter(track=[track_for], is_async=True)
