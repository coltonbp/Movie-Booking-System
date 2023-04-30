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
        self.welcome_label = tk.Label(self, text="Review Show", font=Header2)
        self.welcome_label.grid(row=1, column=1, columnspan=2)

        # Select Show label and dropdown
        self.showTitles = ["Select a Show"]
        self.showVar = tk.StringVar(self)
        self.showVar.set(self.showTitles[0])
        self.show_label = tk.Label(self, text="Show")
        self.show_label.grid(row=2, column=1, columnspan=2)
        self.show_drop = tk.OptionMenu(self, self.showVar, *self.showTitles)
        self.show_drop.grid(row=3, column=1, columnspan=2)

        # Show Title label and entry
        self.reviewDesc_label = tk.Label(self, text="Review")
        self.reviewDesc_label.grid(row=4, column=1, columnspan=2)
        self.reviewDesc_entry = tk.Text(self, width=100, height = 20)
        self.reviewDesc_entry.grid(row=5, column=1, columnspan=2)

        # active show toggle
        self.reviewRatings = [1, 2, 3, 4, 5]
        self.reviewRating = tk.IntVar(self)
        self.reviewRating.set(self.reviewRatings[4])
        self.reviewRate_label = tk.Label(self, text="Rating")
        self.reviewRate_label.grid(row=6, column=1, sticky="ne")
        self.reviewRate_drop = tk.OptionMenu(self, self.reviewRating, *self.reviewRatings)
        self.reviewRate_drop.grid(row=6, column=2, sticky="nw")

        # Submit button
        self.submit_button = tk.Button(self, text="Post Review", width=30, command=lambda: self.btn_submit(controller))
        self.submit_button.grid(row=8, column=1, sticky="s", columnspan=2)

        # Back button
        self.back_button = tk.Button(self, text="Cancel", width=30, command=lambda: self.btn_back(controller))
        self.back_button.grid(row=9, column=1, sticky="s", columnspan=2)

        global thisSelf
        thisSelf = self

        self.refresh()
        
    def refresh(self=thisSelf):
        global thisSelf
        self=thisSelf
        self.showTitles = db.readFrom('shows', '', 'titles', True)
        self.show_drop['menu'].delete(0, 'end')
        for title in self.showTitles:
            self.show_drop['menu'].add_command(label=title, command=tk._setit(self.showVar, title))
            
    
    def btn_submit(self, controller):
        review = [self.showVar.get(), db.readFrom('currentLogin', '', 'name'), self.reviewRating.get(), self.reviewDesc_entry.get("1.0", 'end-1c')]
        db.writeTo('reviews', [review], 'a')
        self.resetForm()
        self.refresh()
        ViewCatalog.main.refresh()
        controller.show_frame(ViewCatalog.main)

    def btn_delete(self):
        idToDelete = self.showVar.get()
        db.deleteFrom('shows', idToDelete)
        self.resetForm()
        self.refresh()

    def btn_back(self, controller):
        #clear all fields to protect privacy
        self.resetForm()
        ViewCatalog.main.refresh()
        controller.show_frame(ViewCatalog.main)

    def resetForm(self):
        self.showVar.set("Select a Show")
        self.reviewDesc_entry.delete("1.0", "end")
        
