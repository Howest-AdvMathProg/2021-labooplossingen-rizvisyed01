import logging
import threading
import json

slow = {
    "Droog": 8,
    "Nat": 5,
}


class ClientHandler(threading.Thread):
    def __init__(self, socket, log_queue):
        threading.Thread.__init__(self)
        self.socket_to_client = socket
        self.log_queue = log_queue

    def run(self):
        io_stream = self.socket_to_client.makefile(mode="rw")
        msg = io_stream.readline().rstrip("\n")
        self.add_msg_to_queue(f"Got data:{msg}")
        speed = self.get_speed(self.format_json(msg), lambda km: float(km) / 3.6)
        self.add_msg_to_queue(f"Calculated speed:{speed}")
        io_stream.write(f"{speed}\n")
        io_stream.flush()
        io_stream.close()

    def format_json(self, string):
        return json.loads(string)

    def get_speed(self, data, converter):
        print(data)
        convertedspeed = converter(data["snelheid"])
        return convertedspeed * data["reactie"] + ((convertedspeed * convertedspeed) / (2 * slow[data["wegdek"]]))

    def add_msg_to_queue(self, msg):
        self.log_queue.put(f"CLH:> {msg}")
