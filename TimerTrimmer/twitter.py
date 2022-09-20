import tweepy
import os


# Authenticate to Twitter
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_SECRET")
consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
# Create API object
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

# Create a tweet
def send_tweet(image, text):
    image.open()
    # api.update_with_media(image, status=text)


if __name__ == "__main__":
    client.create_tweet(text="Testing Creating a Tweet with Tweepy")