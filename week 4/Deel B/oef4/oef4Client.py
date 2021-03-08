import logging
import socket
import sys

logging.basicConfig(level=logging.INFO)

logging.info("Making connection with server...")

# create a socket object
socket_to_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
port = 9999

# connection to hostname on the port.
socket_to_server.connect((host, port))

io_stream_server = socket_to_server.makefile(mode='rw')
msg = input("Geef een boodschap of sluit af met CLOSE: ")
while str.lower(msg) != "close":
    io_stream_server.write(f"{msg}\n")
    io_stream_server.flush()
    recieved = io_stream_server.readline().rstrip('\n')
    print("Antwoord van server: " + recieved)
    msg = input("Geef een boodschap of sluit af met CLOSE: ")


io_stream_server.write("CLOSE\n")
io_stream_server.flush()
logging.info("Close connection with server...")
socket_to_server.close()
