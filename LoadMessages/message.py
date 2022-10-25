import json
import os
import typing
from pathlib import Path

import typer
from azure.storage.queue import QueueClient
from azure.core.exceptions import ResourceExistsError


app = typer.Typer(rich_help_panel="rich")

@app.command()
def load_messages(
    connection_string: str = typer.Option(
            None, "--conn", envvar="AZURE_STORAGE_CONNECTION_STRING",
            help="Connection string for the Azure storage account",
            rich_help_panel="Azure Connection Options"
    ),
    queue_name: str = typer.Option(
        None, "--queue", envvar="AZURE_STORAGE_QUEUE_NAME",
        help="Name of the Azure storage queue",
        rich_help_panel="Azure Connection Options"
    ),
    filepath: typing.Optional[pathlib.Path] = typer.Option(
        None, "-f", "--filepath",
        help="Path to the file containing the messages to load",
        rich_help_panel="Message Options"
    ),
    messages: typing.Optional[list[str]] = typer.Option(
        None, "-m", "--message",
        help="Messages to load",
        rich_help_panel="Message Options"
    ),
    start: typing.Optional[int] = typer.Option(1,
        help="Start index for the messages",
        rich_help_panel="Message Options",
    ),
):
    """
    Iterate through a `messages` optionally applying a formatted messages.
    
    Messages are loaded with the format:
    
    ```
    {INDEX STARTING WITH `start`}: {MESSAGE}
    ```
    """
    # #11 Will change this to just messages and then you'll have to pass in formatting functions to `pre_upload` the message
    for index_, message in enumerate(messages, start=1,): 
        # #11 will check for pre_upload
        yield queue.send_message(f"{index_} - {message}", **kwargs)