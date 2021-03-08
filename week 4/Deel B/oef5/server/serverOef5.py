import logging
import socket
import json

logging.basicConfig(level=logging.INFO)

logging.info(
    "Creating server")
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

serverSocket.bind((host, port))

serverSocket.listen(5)

logging.info("Server started")

slow = {
    "D": 8,
    "N": 5,
}


def format_json(string):
    return json.loads(string)


def get_speed(data, converter):
    print(data)
    convertedspeed = converter(data["snelheid"])
    return convertedspeed * data["reactie"] * ((convertedspeed ** 2) / (2 * slow[data["wegdek"]]))


def to_m_s(kmu):
    return kmu / 3.6


def log_send(var):
    log(f"Sending message: {var}")


def log_rec(var):
    log(f"Recieved message: {var}")


def log(info):
    logging.info(info)


while True:
    log("Waiting for a client....")
    socket_to_client, addr = serverSocket.accept()
    log(f"Got a connection from {addr}")
    my_writer_obj = socket_to_client.makefile(mode='rw')

    msg = my_writer_obj.readline().rstrip("\n")
    log_rec(msg)
    speed = get_speed(format_json(msg), to_m_s)
    log_send(speed)
    my_writer_obj.write(f"{speed}\n")
    my_writer_obj.flush()
    socket_to_client.close()
    logging.info("Connection closed")
