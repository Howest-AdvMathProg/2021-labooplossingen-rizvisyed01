import jsonpickle as jsonpickle
import logging
import socket
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from oef3.data.calcData import *


def show_result(num):
    messagebox.showinfo("Result", f"res = {num}")


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
        data = CalcData(
            snelheid=float(self.entry_snelheid.get()),
            reactie=float(self.entry_reactietijd.get()),
            wegdek=self.cbo_wegdek.get()
        )

        print(jsonpickle.encode(data))
        logging.info(f"Data: {data}")
        self.writer.write(f"{jsonpickle.encode(data)}\n")
        self.writer.flush()

        msg = self.writer.readline().rstrip("\n")
        res = jsonpickle.decode(msg)
        show_result(res)

    def show_image(self, img_stream):
        self.canvas = Canvas(self, width=300, height=300)
        

    def close_connection(self):
        self.conn.close()


logging.basicConfig(level=logging.INFO)
root = Tk()
app = Window(root)
root.mainloop()
