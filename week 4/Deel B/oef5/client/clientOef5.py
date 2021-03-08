import logging
import socket
import json

data = {
    "snelheid": 90.0,
    "reactie": 1.0,
    "wegdek": "D",
}

logging.basicConfig(level=logging.INFO)

logging.info("Making connection with server...")

# create a socket object
socket_to_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
port = 9999

# connection to hostname on the port.
socket_to_server.connect((host, port))

print("Volgende data wordt verstuurd: " + json.dumps(data))
io_stream_server = socket_to_server.makefile(mode='rw')
io_stream_server.write(f"{json.dumps(data)}\n")
io_stream_server.flush()

recieved = io_stream_server.readline().rstrip('\n')
logging.info(f"De snelheid is: {recieved}")

logging.info("Close connection with server...")
socket_to_server.close()
