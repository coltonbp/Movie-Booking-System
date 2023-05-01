import tkinter as tk
from tkinter import ttk
import csv
import fetch as db
import ViewCatalog

Header1 = ("Helvetica", 25)
Header2 = ("Helvetica", 16)
LargeText = ("Helvetica", 14)

thisSelf=None

class main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global thisSelf
        thisSelf = self

        #column and row config
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
        self.columnconfigure(2, weight=4)
        self.columnconfigure(3, weight=1)

        # Title label
        self.title_label = tk.Label(self, text="West TX Movie Booking System", font=Header1)
        self.title_label.grid(row=0, column=1, columnspan=2)

        # Registration label
        self.welcome_label = tk.Label(self, text="View Report", font=Header2)
        self.welcome_label.grid(row=1, column=1, columnspan=2)

        # Back button
        self.back_button = tk.Button(self, text="<-- Go Back", width=10, command=lambda: self.btn_back(controller))
        self.back_button.grid(row=0, column=0, sticky="nw")

        self.refresh()
    def refresh(self=thisSelf):
        global thisSelf
        self = thisSelf

        shows = db.readFrom('shows', '', '', True)
        tickets = db.readFrom('tickets', '', '', True)
        iRow = 2
        for show in shows:
            sales = 0
            for ticket in tickets:
                if ticket[2] == show[0]:
                    sales = sales + 1
            self.showtitle_label = tk.Label(self, text=f'{show[0]} - {sales} tickets sold.', font=Header2)
            self.showtitle_label.grid(row=iRow, column=1, columnspan=2)
            iRow = iRow + 1
            self.showbreak_label = tk.Label(self, text="----------")
            self.showbreak_label.grid(row=iRow, column=1, columnspan=2)
            iRow = iRow + 1

    def btn_back(self, controller):
        ViewCatalog.main.refresh()
        controller.show_frame(ViewCatalog.main)
        
