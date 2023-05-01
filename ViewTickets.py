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
        self.welcome_label = tk.Label(self, text="View Your Tickets", font=Header2)
        self.welcome_label.grid(row=1, column=1, columnspan=2)

        # Back button
        self.back_button = tk.Button(self, text="<-- Go Back", width=10, command=lambda: self.btn_back(controller))
        self.back_button.grid(row=0, column=0, sticky="nw")

        self.displayedTickets = []
        self.refresh()
        
    def refresh(self=thisSelf):
        global thisSelf
        self = thisSelf
        print("displayed tickets")
        print(self.displayedTickets)
        i = 0
        for ticket in self.displayedTickets:
            for element in ticket:
                element.destroy()
        self.displayedTickets = []

        shows = db.readFrom('shows', '', '', True)
        tickets = db.readFrom('tickets', '', '', True)
        user = db.readFrom('currentLogin', '', '')
        print(user)
        iRow = 2
        for show in shows:
            sales = 0
            for ticket in tickets:
                if ticket[1] == user[0] and ticket[2] == show[0]:
                    thisTicket = []
                    self.showtitle_label = tk.Label(self, text=f'{show[0]} @ {ticket[3]}', font=Header1)
                    self.showtitle_label.grid(row=iRow, column=1, columnspan=2)
                    thisTicket.append(self.showtitle_label)
                    iRow = iRow + 1
                    ticketTxt = f"Name: {user[2]}\tBarcode: {ticket[4]} \t(qty: {ticket[5]})"
                    self.ticket_label= tk.Label(self, text=ticketTxt, font=LargeText, justify="left")
                    self.ticket_label.grid(row=iRow, column=1, columnspan=2)
                    thisTicket.append(self.ticket_label)
                    iRow = iRow + 1
                    self.showbreak_label = tk.Label(self, text="----------")
                    self.showbreak_label.grid(row=iRow, column=1, columnspan=2)
                    thisTicket.append(self.showbreak_label)
                    iRow = iRow + 1
                    self.displayedTickets.append(thisTicket)

    def btn_back(self, controller):
        self.refresh()
        ViewCatalog.main.refresh()
        controller.show_frame(ViewCatalog.main)
        
