import os
from azure.storage.queue import QueueClient

conn_string = os.environ.get('AZURE_STORAGE_CONNECTION_STRING')


def load_queue(name: str) -> QueueClient:
    """
    source: https://learn.microsoft.com/en-us/azure/storage/queues/storage-python-how-to-use-queue-storage?tabs=python%2Cenvironment-variable-windows
    """
    # Create a unique name for the queue
    return QueueClient.from_connection_string(conn_string, name)