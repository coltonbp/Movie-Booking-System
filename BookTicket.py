import tkinter as tk
from tkinter import ttk
import csv
import fetch as db
import LogIn
import ViewCatalog

Header1 = ("Helvetica", 25)
Header2 = ("Helvetica", 16)
LargeText = ("Helvetica", 14)

thisSelf=None

class main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #column and row config
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
        self.columnconfigure(2, weight=4)
        self.columnconfigure(3, weight=1)

        # Title label
        self.title_label = tk.Label(self, text="West TX Movie Booking System", font=Header1)
        self.title_label.grid(row=0, column=1, columnspan=2)

        # Registration label
        self.welcome_label = tk.Label(self, text="Book Ticket", font=Header2)
        self.welcome_label.grid(row=1, column=1, columnspan=2)

        # Select Show label and dropdown
        self.showTimes = ["Placehold"]
        self.showVar = tk.StringVar()
        self.showVar.set("placehold")
        self.show_label = tk.Label(self, text="Time")
        self.show_label.grid(row=6, column=1, sticky="e")
        self.show_drop = tk.OptionMenu(self, self.showVar, *self.showTimes)
        self.show_drop.grid(row=6, column=2, sticky="w")

        # Show Title label and entry
        self.showTitle_label = tk.Label(self, text='', font=Header1)
        self.showTitle_label.grid(row=2, column=1, columnspan=2)
        self.showDesc_label = tk.Label(self, text='', wraplength=400, font=LargeText)
        self.showDesc_label.grid(row=3, column=1, columnspan=2)

        # Submit button
        self.submit_button = tk.Button(self, text="Book Ticket", width=30, command=lambda: self.btn_submit(controller))
        self.submit_button.grid(row=9, column=1, sticky="s", columnspan=2)

        # Back button
        self.back_button = tk.Button(self, text="Cancel", width=30, command=lambda: self.btn_back(controller))
        self.back_button.grid(row=10, column=1, sticky="s", columnspan=2)

        global thisSelf
        thisSelf = self

        #self.refresh()
        
    def refresh(self=thisSelf):
        global thisSelf
        self=thisSelf
        self.showTimes = db.readFrom('shows', self.showTitle, 'times').split(",")
        print(self.showTimes)
        self.show_drop['menu'].delete(0, 'end')
        for time in self.showTimes:
            time = time.strip()
            self.show_drop['menu'].add_command(label=time, command=tk._setit(self.showVar, time))
        self.showVar.set(self.showTimes[0])
        self.showTitle_label.config(text=self.showTitle)
        self.showDesc_label.config(text=self.showDesc)
            
    def initShow(self, showTitle):
        global thisSelf
        self = thisSelf
        self.showTitle = showTitle
        self.show = db.readFrom('shows', showTitle, '')
        self.showDesc = self.show[2]
        self.showTimes = self.show[3].split(",")
        self.resetForm()
    
    def btn_submit(self, controller):
        ticket = [len(db.readFrom('tickets', '', '', True)) + 1, db.readFrom('currentLogin', '', '')[0], self.showTitle, self.showVar.get()]
        db.writeTo('tickets', [ticket], 'a')
        self.resetForm()
        self.refresh()
        ViewCatalog.main.refresh()
        controller.show_frame(ViewCatalog.main)

    def btn_back(self, controller):
        #clear all fields to protect privacy
        self.resetForm()
        ViewCatalog.main.refresh()
        controller.show_frame(ViewCatalog.main)

    def resetForm(self):
        self.showVar.set("Select a Time.")
        
        
