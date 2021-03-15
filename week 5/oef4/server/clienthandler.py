import logging
import threading
import jsonpickle as jsonpickle

from oef3.data.calcData import *


class ClientHandler(threading.Thread):
    def __init__(self, socket, log_queue):
        threading.Thread.__init__(self)
        self.socket_to_client = socket
        self.log_queue = log_queue

    def run(self):
        io_stream = self.socket_to_client.makefile(mode="rw")
        msg = io_stream.readline().rstrip("\n")
        self.add_msg_to_queue(f"Got data:{msg}")
        data = jsonpickle.decode(msg)
        print("hier:", type(data))
        data.calcStopAfstand()
        print("hier:", type(data))
        self.add_msg_to_queue(f"Calculated speed:{data.get_dist()}")
        io_stream.write(f"{jsonpickle.encode(data)}\n")
        io_stream.flush()
        io_stream.close()

    def add_msg_to_queue(self, msg):
        self.log_queue.put(f"CLH:> {msg}")
