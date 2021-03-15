import logging
import socket
import json
from clienthandler import *
import threading

logging.basicConfig(level=logging.INFO)

logging.info(
    "Creating server")
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

serverSocket.bind((host, port))

serverSocket.listen(5)

logging.info("Server started")


while True:
    logging.info("Waiting for a client....")
    socket_to_client, addr = serverSocket.accept()
    logging.info((f"Got a connection from {addr}"))
    client = ClientHandler(socket_to_client)
    client.start()

    logging.info(f"Server ok: current thread count: {threading.active_count()}")
