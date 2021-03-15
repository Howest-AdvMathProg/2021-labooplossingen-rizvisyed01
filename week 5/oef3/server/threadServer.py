import logging
import socket
import threading

from clienthandler import *

logging.basicConfig(level=logging.INFO)


class ThreadServer(threading.Thread):

    def __init__(self, host, port, messages_queue):
        threading.Thread.__init__(self, name="Thread-Server")
        self.__is_connected = False
        self.host = host
        self.port = port
        self.log_queue = messages_queue

    @property
    def is_connected(self):
        return self.__is_connected

    def init_server(self):
        # create a socket object
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.bind((self.host, self.port))
        self.serversocket.listen(5)
        self.__is_connected = True
        self.print_bericht_gui_server("SERVER STARTED")

    def close_server_socket(self):
        self.serversocket.close()

    def run(self):
        number_received_message = 0
        try:
            while True:
                self.print_bericht_gui_server("waiting for a new client...")
                socket_to_client, addr = self.serversocket.accept()
                self.print_bericht_gui_server(f"Got a connection from {addr}")

                # is dit een pointer?
                clh = ClientHandler(socket_to_client, self.log_queue)
                clh.start()
                self.print_bericht_gui_server(f"Current Thread count: {threading.active_count()}.")

        except Exception as ex:
            logging.error(ex)
            self.print_bericht_gui_server("Serversocket afgesloten")

    def print_bericht_gui_server(self, message):
        self.log_queue.put(f"Server:> {message}")
