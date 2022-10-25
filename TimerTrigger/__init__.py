import datetime
import json
import logging
import os
from io import BytesIO

import azure.functions as func
import spacy
from azqueuetweeter import QueueTweeter, storage, twitter
from .image import overlay_text

nlp = spacy.load("assets/en_core_web_sm-3.4.0/en_core_web_sm/en_core_web_sm-3.4.0")

image_path = os.environ.get("IMAGE_TEMPLATE_PATH")
conn_string = os.environ.get("AZURE_STORAGE_CONNECTION_STRING")
queue_name = os.environ.get("AZURE_STORAGE_QUEUE_NAME")

sa = storage.Auth(connection_string=conn_string, queue_name=queue_name)
ta = twitter.Auth(
    consumer_key=os.environ.get("TWITTER_CONSUMER_KEY"),
    consumer_secret=os.environ.get("TWITTER_CONSUMER_SECRET"),
    access_token=os.environ.get("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.environ.get("TWITTER_ACCESS-TOKEN_SECRET"),
)


def segment_message(msg_test: str):
    if len(msg_test) < 260:
        return msg_test
    doc = nlp(msg_test)

    sent_msg = str()
    for sent in doc.sents:
        if len(sent_msg + str(sent)) < 260:
            sent_msg += str(sent)
        else:
            sent_msg += "..."
            return sent_msg


def gen_image(msg: dict) -> BytesIO:
    img = overlay_text(
        msg["index"], msg["text"], image_path=image_path
    )  # TODO: #9 Change to path stored in environment variable
    image = BytesIO()
    img.save(image, format="PNG")
    image.seek(0)
    return image


def load_message(msg: str) -> dict:
    _msg = json.loads(msg)
    return {
        "text": f"{_msg['index']}: {segment_message(_msg['text'])} #31DaysOfNeurodivergence",
        "file": gen_image(_msg),
        "filename": f"{_msg['index']}{_msg['text'][:10]}",
    }


def main(mytimer: func.TimerRequest) -> None:
    queue = QueueTweeter(storage_auth=sa, twitter_auth=ta)
    msg = queue.send_next_message(
        message_transformer=load_message, preview_mode=False, delete_after=False
    )

    # Message is in format "Index - Text"
    logging.info(f"{msg} triggered at {datetime.datetime.utcnow()}")
