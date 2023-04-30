import tkinter as tk
from tkinter import ttk
import LogIn
import CreateAcc
import ViewCatalog

Header1 = ("Helvetica", 16)
Header2 = ("Helvetica", 12)

class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("West TX")
        self.geometry("1000x750")

        container = tk.Frame(self, width=1000, height=800)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for page in (LogIn.main, CreateAcc.main, ViewCatalog.main):
            frame = page(container, self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(LogIn.main)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

    def refresh_frame(self, container):
        frame = self.frames[container]
        frame.refresh()

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
