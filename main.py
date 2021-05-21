import tweepy
from auth import APITW
from classes import MyStreamListener

try:
    user_info = APITW.verify_credentials()
    print("Authentication OK")
    name = user_info._json['name']
    user_name = user_info._json['screen_name']
    user_id = user_info._json['id_str']
    followers = user_info._json['followers_count']
    followings = user_info._json['friends_count']
    joined = user_info._json['created_at']
    tweet_count = user_info._json['statuses_count']
    print('Name:'+name, '\nUserName: '+ user_name, '\nID: '+ user_id, '\nFollowers: '+followers, '\nFollowing: '+followings,"\nJoined: " + joined,"\nTweet Count: " + tweet_count)
except:
    print("Error during authentication")

track_for = input("Please Eenter the hashtag to stream (ex: #python): ")
tweets_listener = MyStreamListener(APITW)
stream = tweepy.Stream(APITW.auth, tweets_listener)
stream.filter(track=[track_for], is_async=True)
