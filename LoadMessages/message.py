import os
import typing
import typer
from pathlib import Path
from azure.storage.queue import QueueClient


conn_string = os.environ.get('AZURE_STORAGE_CONNECTION_STRING')

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
    for index_, message in enumerate(messages, start=1,): 
        # #11 will check for pre_upload
        yield queue.send_message(f"{index_} - {message}", **kwargs)


def main(filepath: Path, queuename: str):
    queue_client = QueueClient.from_connection_string(conn_string, queuename)
    messages = filepath.read_text().splitlines()
    for message in load_messages(messages, queue_client):
        ...

if __name__ == "__main__":
    typer.run(main)