import json
import os
import typing
from pathlib import Path

import typer
from azure.storage.queue import QueueClient


def load_messages(
    messages: typing.Sequence[str],
    queue: QueueClient,
    # pre-upload: typing.Optional[list[function]] = None, # TODO: #11 Add Formatting Rules
    **kwargs,
):
    """
    Iterate through a `messages` optionally applying a formatted messages.

    """
    # #11 Will change this to just messages and then you'll have to pass in formatting functions to `pre_upload` the message
    for index_, message in enumerate(
        messages,
        start=1,
    ):
        # #11 will check for pre_upload
        yield queue.send_message(
            json.dumps({"index": index_, "text": message.strip()}), time_to_live=-1
        )


def main(filepath: Path):
    queue_client = QueueClient.from_connection_string(conn_string, queue_name)
    messages = filepath.read_text().splitlines()
    for message in load_messages(messages, queue_client):
        ...



if __name__ == "__main__":
    conn_string = os.environ.get("AZURE_STORAGE_CONNECTION_STRING")
    queue_name = os.environ.get("AZURE_STORAGE_QUEUE_NAME")
    typer.run(main)
