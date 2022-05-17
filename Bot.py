import time
import tweepy
import datetime
import Api

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


def post_tweet(tweet):
    api.update_status(tweet)

git init
while True:
    current_hour = datetime.datetime.now().hour
    if current_hour % 2 == 0:
        try:
            post_tweet(Api.get_cat_data())
        except:
            pass
    else:
        post_tweet(Api.get_dog_data())
    print("tweet sent")
    time.sleep(30)
    print("sending tweet")

