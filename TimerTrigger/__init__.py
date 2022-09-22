import datetime
import logging
from storage import load_queue
from image import overlay_text
import azure.functions as func
from twitter import send_tweet
from io import BytesIO


def main(mytimer: func.TimerRequest) -> None:
    queue = load_queue("31daysofndqueue")
    queue.send_message("2 - This is a numbered queue message")
    msg = queue.receive_messages().next()
    # Message is in format "Index - Text"
    index_, text = msg.content.split(" - ", maxsplit=1)
    img = overlay_text(index_, text, image_path="./assets/test_cat.jpeg")
    image = BytesIO()
    img.save(image, format="JPEG")
    image.seek(0)
    send_tweet(image=image, text=msg.content)
    logging.info(f"{msg.content} triggered at {datetime.datetime.utcnow()}")
    queue.delete_message(msg.id, msg.pop_receipt)


if __name__ == "__main__":
    main(None)