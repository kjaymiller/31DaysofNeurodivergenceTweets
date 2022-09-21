import datetime
import logging
from storage import load_queue
from image import overlay_text
import azure.functions as func
from twitter import send_tweet
from io import BytesIO


def main(mytimer: func.TimerRequest) -> None:
    queue = load_queue("31daysofndqueue")
    queue.send_message("This is a queued message from Azure Storage Queue.")
    msg = queue.receive_messages().next()
    img = overlay_text(1, msg.content, image_path="./assets/test_cat.jpeg")
    image = BytesIO()
    img.save(image, format="JPEG")
    
    send_tweet(image, msg.content)
    logging.info(f"{msg.content} triggered at {datetime.datetime.utcnow()}")
    queue.delete_message(msg.id, msg.pop_receipt)


if __name__ == "__main__":
    main(None)