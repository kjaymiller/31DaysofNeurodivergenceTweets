import tweepy
import os
from uuid import uuid4
import logging

# Authenticate to Twitter
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_SECRET")
consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")

auth = tweepy.OAuth1UserHandler(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

api = tweepy.API(auth)

# Create API 2.0 object
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

# Create a tweet
def send_tweet(image: bytes, text: str):
    media = api.media_upload(filename="test_image.jpeg", file=image)
    return client.create_tweet(text=text, media_ids=[media.media_id])
