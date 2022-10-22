import os
import typing
import typer
import pathlib
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
    queue = QueueClient.from_connection_string(connection_string, queue_name)
    
    try:
        queue.create_queue()
    
    except ResourceExistsError:
        pass
    
    # if queue doesn't exist, create it

    if filepath:
        with open(filepath, "r") as f:
            messages = f.readlines()
    
    for index_, message in enumerate(messages, start=start): 
        # #11 will check for pre_upload
        queue.send_message(f"{index_} - {message}", time_to_live=60*60*24*1)

        typer.echo(f"Sent {len(messages)} messages")

@app.command()   
def clear_messages(
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
):
    """
    Clear all messages from a queue
    """
    queue = QueueClient.from_connection_string(connection_string, queue_name)
    queue.clear_messages()
    typer.echo(f"All messages from \"{queue_name}\" cleared")

if __name__ == "__main__":
    app()