import logging
import threading
import json

slow = {
    "Droog": 8,
    "Nat": 5,
}


class ClientHandler(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.socket_to_client = socket

    def run(self):
        io_stream = self.socket_to_client.makefile(mode="rw")
        msg = io_stream.readline().rstrip("\n")

        speed = self.get_speed(self.format_json(msg), lambda km: float(km) / 3.6)
        io_stream.write(f"{speed}\n")
        io_stream.flush()
        io_stream.close()

    def format_json(self, string):
        return json.loads(string)

    def get_speed(self, data, converter):
        print(data)
        convertedspeed = converter(data["snelheid"])
        return convertedspeed * data["reactie"] + ((convertedspeed * convertedspeed) / (2 * slow[data["wegdek"]]))
