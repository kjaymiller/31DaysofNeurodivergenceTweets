import os
from azure.storage.queue import QueueClient

conn_string = os.environ.get('AZURE_STORAGE_CONNECTION_STRING')


def load_queue(name: str) -> QueueClient:
    """
    source: https://learn.microsoft.com/en-us/azure/storage/queues/storage-python-how-to-use-queue-storage?tabs=python%2Cenvironment-variable-windows
    """
    # Create a unique name for the queue
    return QueueClient.from_connection_string(conn_string, name)


def insert_message(queue_client: QueueClient, message: str) -> None:
    return queue_client.send_message(message, time_to_live=-1)

if __name__ == "__main__":
    queue = load_queue("31daysofndqueue")
    # insert_message(queue, "Hello World")
    # insert_message(queue, "Hello Moon")
    # insert_message(queue, "Hello Space")
    msg = queue.receive_messages().next()
    print(msg.content, msg.id, msg.pop_receipt)
    queue.delete_message(msg.id, msg.pop_receipt)