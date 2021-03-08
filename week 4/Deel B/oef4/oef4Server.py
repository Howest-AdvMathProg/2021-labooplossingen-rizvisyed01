import logging
import socket

logging.basicConfig(level=logging.INFO)

logging.info(
    "Creating server")
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

serverSocket.bind((host, port))

serverSocket.listen(5)

logging.info("Server started")

active = False

while True:
    logging.info("Waiting for a client....")
    socket_to_client, addr = serverSocket.accept()
    logging.info(f"Got a connection from {addr}")
    my_writer_obj = socket_to_client.makefile(mode='rw')
    active = True

    while active:
        msg = my_writer_obj.readline().rstrip("\n")
        logging.info(f"Recieved message: {msg}")
        if str.lower(msg) == "close":
            active = False
        else:
            my_writer_obj.write(f"{msg}\n")
            my_writer_obj.flush()

    socket_to_client.close()
    logging.info("Connection closed")
