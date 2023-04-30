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

        #column and row config
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
        self.columnconfigure(2, weight=4)
        self.columnconfigure(3, weight=1)

        # Title label
        self.title_label = tk.Label(self, text="West TX Movie Booking System", font=Header1)
        self.title_label.grid(row=0, column=1, columnspan=2)

        # Registration label
        self.welcome_label = tk.Label(self, text="Manage Shows", font=Header2)
        self.welcome_label.grid(row=1, column=1, columnspan=2)

        # Select Show label and dropdown
        self.showTitles = ["+ Add New Show"]
        self.showVar = tk.StringVar(self)
        self.showVar.set(self.showTitles[0])
        self.showVar.trace("w", self.btn_showdrop)
        self.show_label = tk.Label(self, text="Show")
        self.show_label.grid(row=2, column=1, columnspan=2)
        self.show_drop = tk.OptionMenu(self, self.showVar, *self.showTitles)
        self.show_drop.grid(row=3, column=1, columnspan=2)

        # Show Title label and entry
        self.showtitle_label = tk.Label(self, text="Show Title")
        self.showtitle_label.grid(row=4, column=1, columnspan=2)
        self.showtitle_entry = tk.Entry(self, width=30)
        self.showtitle_entry.grid(row=5, column=1, columnspan=2)

        # Show Desc label and entry
        self.showdesc_label = tk.Label(self, text="Show Description")
        self.showdesc_label.grid(row=6, column=1, columnspan=2)
        self.showdesc_entry = tk.Entry(self, width=30)
        self.showdesc_entry.grid(row=7, column=1, columnspan=2)

        # Show times label and entry
        self.showtimes_label = tk.Label(self, text="Show Times (comma seperated)")
        self.showtimes_label.grid(row=8, column=1, columnspan=2)
        self.showtimes_entry = tk.Entry(self, width=30)
        self.showtimes_entry.grid(row=9, column=1, columnspan=2)

        # active show toggle
        self.showActive = tk.IntVar(self)
        self.active_check = tk.Checkbutton(self, text="Show Active", variable=self.showActive)
        self.active_check.grid(row=10, column=1, columnspan=2)

        # Submit button
        self.submit_button = tk.Button(self, text="Create/Edit Show", width=30, command=lambda: self.btn_submit(controller))
        self.submit_button.grid(row=11, column=1, columnspan=2)

        # Back button
        self.back_button = tk.Button(self, text="Go Back", width=30, command=lambda: self.btn_back(controller))
        self.back_button.grid(row=12, column=1, sticky="ne")

        # Delete button
        self.del_button = tk.Button(self, text="Delete Show", width=30, command=lambda: self.btn_delete(), state=tk.DISABLED)
        self.del_button.grid(row=12, column=2, sticky="nw")

        global thisSelf
        thisSelf = self

        self.refresh()
        
    def refresh(self=thisSelf):
        global thisSelf
        self=thisSelf
        self.showTitles = db.readFrom('shows', '', 'titles', True)
        self.showTitles.append("+ Add New Show")
        self.show_drop['menu'].delete(0, 'end')
        for title in self.showTitles:
            self.show_drop['menu'].add_command(label=title, command=tk._setit(self.showVar, title))
            
    
    def btn_submit(self, controller):
        shows = db.readFrom('shows', '', '', True)
        if self.showVar.get() == "+ Add New Show":
            print("create show")
            newShow = [self.showtitle_entry.get(), self.showActive.get(), self.showdesc_entry.get(), self.showtimes_entry.get()]
            shows.append(newShow)
        else:
            print("edit show")
            for show in shows:
                if show[0] == self.showVar.get():
                    show[0] = self.showtitle_entry.get()
                    show[1] = self.showActive.get()
                    show[2] = self.showdesc_entry.get()
                    show[3] = self.showtimes_entry.get()
        shows.sort()
        print("shows: " + str(shows))
        db.writeTo('shows', shows, 'w')
        self.resetForm()
        self.refresh()
        ViewCatalog.main.refresh()
        controller.show_frame(ViewCatalog.main)

    def btn_delete(self):
        print("delete")
        idToDelete = self.showVar.get()
        db.deleteFrom('shows', idToDelete)
        self.resetForm()
        self.refresh()

    def btn_back(self, controller):
        print("back")
        #clear all fields to protect privacy
        self.resetForm()
        ViewCatalog.main.refresh()
        controller.show_frame(ViewCatalog.main)

    def btn_showdrop(self, *args):
        showToEdit = self.showVar.get()
        self.showtitle_entry.delete(0, 'end')
        self.showdesc_entry.delete(0, 'end')
        self.showtimes_entry.delete(0, 'end')
        if showToEdit == "+ Add New Show":
            self.del_button.config(state=tk.DISABLED)
        else:
            showInfo = db.readFrom('shows', showToEdit, '')
            self.showtitle_entry.insert(0, showInfo[0])
            self.showdesc_entry.insert(0, showInfo[2])
            self.showtimes_entry.insert(0, showInfo[3])
            if showInfo[1] == "1":
                self.active_check.select()
            else:
                self.active_check.deselect()
            self.del_button.config(state=tk.NORMAL)
            
    def selectShow(self, showToSelect):
        global thisSelf
        self = thisSelf
        self.showVar.set(showToSelect)

    def resetForm(self):
        self.showVar.set("+ Add New Show")
        self.showtitle_entry.delete(0, 'end')
        self.showdesc_entry.delete(0, 'end')
        self.showtimes_entry.delete(0, 'end')
        self.del_button.config(state=tk.DISABLED)
        
