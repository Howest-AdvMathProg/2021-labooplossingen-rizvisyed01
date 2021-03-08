import logging
import socket
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import json


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.host = socket.gethostname()
        self.port = 9999
        self.makeConnnectionWithServer()

    def init_window(self):
        self.master.title("Stopafstand")
        self.pack(fill=BOTH, expand=1)

        Label(self, text="Snelheid (km/u):").grid(row=0)
        Label(self, text="Reactietijd (sec):", pady=10).grid(row=1)
        Label(self, text="Type wegdek:", pady=10).grid(row=2)

        self.entry_snelheid = Entry(self, width=40)
        self.entry_reactietijd = Entry(self, width=40)
        self.entry_wegdek = Entry(self, width=40)
        self.entry_snelheid.grid(row=0, column=1, sticky=E + W, pady=(5, 5))
        self.entry_reactietijd.grid(row=1, column=1, sticky=E + W)

        choices = ('Droog',
                   'Nat')
        self.cbo_wegdek = Combobox(self, state="readonly", width=40)
        self.cbo_wegdek['values'] = choices
        self.cbo_wegdek.grid(row=2, column=1, sticky=E + W)
        Label(self, text="km/u").grid(row=0, column=2)
        Label(self, text="sec", pady=10).grid(row=1, column=2)
        self.buttonCalculate = Button(self, text="Bereken stopafstand", command=self.calculateStopafstand)
        self.buttonCalculate.grid(row=3, column=0, columnspan=3, pady=(0, 5), padx=(5, 5), sticky=N + S + E + W)
        Grid.rowconfigure(self, 2, weight=1)
        Grid.columnconfigure(self, 1,
                             weight=1)

    def __del__(self):
        self.close_connection()

    def makeConnnectionWithServer(self):
        socket_to_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn = socket_to_server.connect((self.host, self.port))
        self.writer = socket_to_server.makefile(mode='rw')

    def calculateStopafstand(self):
        data = {
            "snelheid": float(self.entry_snelheid.get()),
            "reactie": float(self.entry_reactietijd.get()),
            "wegdek": self.cbo_wegdek.get(),
        }
        logging.info(f"Data: {data}")
        self.writer.write(f"{json.dumps(data)}\n")
        self.writer.flush()


    def close_connection(self):
        self.conn.close()


logging.basicConfig(level=logging.INFO)
root = Tk()
app = Window(root)
root.mainloop()
