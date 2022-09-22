import datetime
import logging
from storage import load_queue
from image import overlay_text
import azure.functions as func
from twitter import send_tweet
from io import BytesIO
import os

image_path = os.environ.get("IMAGE_TEMPLATE_PATH")

def main(mytimer: func.TimerRequest) -> None:
    queue = load_queue("31daysofndqueue")
    msg = queue.receive_messages().next() # TODO: #10 Add Logic to check queue count
    
    # Message is in format "Index - Text"
    index_, text = msg.content.split(" - ", maxsplit=1)
    img = overlay_text(index_, text, image_path=image_path) # TODO: #9 Change to path stored in environment variable
    image = BytesIO()
    img.save(image, format="JPEG")
    image.seek(0)
    send_tweet(image=image, text=msg.content)
    logging.info(f"{msg.content} triggered at {datetime.datetime.utcnow()}")
    queue.delete_message(msg.id, msg.pop_receipt)


if __name__ == "__main__":
    main(None)