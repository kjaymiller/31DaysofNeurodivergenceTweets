import typing
from storage import load_queue


def load_messages(messages: typing.Sequence[str], queue_name: QueueClient, format: typing.Optional[function]):
    """Iterate through a queue and add the formatted messages"""
    
    for index_, message in enumerate(messages, start=1):
        azaueue.send_message(f"{index_} - {message}", time_to_live=-1)

    return azqueue

def split_text()