import time
import threading
from tkinter import * 
from tkinter import ttk

class PomodoTimer:
    def __init__(self):
        self.root = Tk()
        self.root.title("Relok Pomodoro")
        self.root.geometry("400x400")
        self.root.resizable(False,False)
        self.root.iconphoto("wn", PhotoImage(file="./Icon/icon.png"))

        self.s = ttk.Notebook()

        self.root.mainloop()
self.tabs = tt
PomodoTimer()