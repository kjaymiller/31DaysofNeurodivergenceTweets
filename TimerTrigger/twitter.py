import typing
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
def send_tweet(
    text: str,
    image_name: str,
    image_data: typing.Optional[bytes]=None,
    api: tweepy.API=api,
    client: tweepy.Client=client,
):
    """
    Send a tweet with an image.
    
    Note:
        if image_data is None, then it will try to open the image from the `image_name` path.

    Note:
        if api and client are None, then it will look for `TWITTER_ACCESS_TOKEN`, `TWITTER_ACCESS_SECRET`, `TWITTER_CONSUMER_KEY`, `TWITTER_CONSUMER_SECRET` in the environment variables.
    """
    media = api.media_upload(filename=image_name, file=image_data)
    return client.create_tweet(text=text, media_ids=[media.media_id])
