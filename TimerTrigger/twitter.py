import tweepy
import os
from uuid import uuid4
import logging

# Authenticate to Twitter
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_SECRET")
consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

# Create API 2.0 object
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

# Create a tweet
def send_tweet(image, text):
    media = api.media_upload(filename=str(uuid4())+".jpg", file=image, alt_text=text)
    logging.error(client.create_tweet(text=text, media_ids=[media]))
