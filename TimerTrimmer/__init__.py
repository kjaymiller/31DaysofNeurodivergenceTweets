import datetime
import logging
from .storage import load_queue, insert_message
from .image import overlay_text
import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    queue = load_queue("31daysofndqueue")
    msg = queue.receive_messages().next()
    overlay_text(msg.content)
    queue.delete_message(msg.id, msg.pop_receipt)
    logging.info('Python timer trigger function ran at %s', utc_timestamp)
