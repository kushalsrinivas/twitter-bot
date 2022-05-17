import time
import tweepy
import datetime
import Api

consumer_key = 'KXrvAm7zPto1RAmm14nr1iFT0'
consumer_secret = 'wOFuB3Pw8ho1Y1wXsOWS4ceMG84iTAzNzjaPaxriTq0CeeckRV'
access_token = '1524709195970670592-9AGYTKdJpxfoInoe7TN7CAupBL8YpM'
access_token_secret = 'DdvxTmxBSnpieIf7Vk5nLTG2Tm6zqZq35vIuTwzbSBUHl'
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

