import threading
from tkinter import *

from serverWindow import *

def callback():
    # test
    # threads overlopen
    print("Active threads:")
    for thread in threading.enumerate():
        print(f">Thread name is {thread.getName()}.")
    gui_server.afsluiten_server()
    root.destroy()

root = Tk()
root.geometry("600x500")
gui_server = ServerWindow(root)
root.protocol("WM_DELETE_WINDOW", callback)
root.mainloop()
