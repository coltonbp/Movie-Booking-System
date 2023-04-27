import tkinter as tk
from tkinter import ttk
import csv
import LogIn

Header1 = ("Helvetica", 25)
Header2 = ("Helvetica", 16)
LargeText = ("Helvetica", 14)

class main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #column and row config
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=8)
        self.columnconfigure(2, weight=1)

        # Title label
        self.title_label = tk.Label(self, text="West TX Movie Booking System", font=Header1)
        self.title_label.grid(row=0, column=1)

        # Registration label
        self.welcome_label = tk.Label(self, text="Account Registration", font=Header2)
        self.welcome_label.grid(row=1, column=1)

        # Username label and entry
        self.username_label = tk.Label(self, text="Email Address")
        self.username_label.grid(row=2, column=1)
        self.username_entry = tk.Entry(self, width=30)
        self.username_entry.grid(row=3, column=1)

        # Password label and entry
        self.password_label = tk.Label(self, text="Password")
        self.password_label.grid(row=4, column=1)
        self.password_entry = tk.Entry(self, width=30, show="*")
        self.password_entry.grid(row=5, column=1)

        # Confirm password label and entry
        self.passwordconfirm_label = tk.Label(self, text="Confirm Password")
        self.passwordconfirm_label.grid(row=6, column=1)
        self.passwordconfirm_entry = tk.Entry(self, width=30, show="*")
        self.passwordconfirm_entry.grid(row=7, column=1)

        # Name label and entry
        self.name_label = tk.Label(self, text="Name")
        self.name_label.grid(row=8, column=1)
        self.name_entry = tk.Entry(self, width=30)
        self.name_entry.grid(row=9, column=1)
        
        # Home address label and entry
        self.home_label = tk.Label(self, text="Home Address")
        self.home_label.grid(row=10, column=1)
        self.home_entry = tk.Entry(self, width=30)
        self.home_entry.grid(row=11, column=1)
        
        # Phone number label and entry
        self.phone_label = tk.Label(self, text="Phone Number")
        self.phone_label.grid(row=12, column=1)
        self.phone_entry = tk.Entry(self, width=30)
        self.phone_entry.grid(row=13, column=1)
        
        # Error message label
        self.error_label = tk.Label(self, text="", fg="red")
        self.error_label.grid(row=14, column=1)

        # Submit button
        self.submit_button = tk.Button(self, text="Create Account", width=30, command=lambda: self.btn_submit(controller))
        self.submit_button.grid(row=15, column=1)

        # Back button
        self.back_button = tk.Button(self, text="Go Back", width=30, command=lambda: self.btn_back(controller))
        self.back_button.grid(row=16, column=1)
        
    def btn_submit(self, controller):
        print("submit")
        #get data from entry fields
        username = self.username_entry.get()
        password = self.password_entry.get()
        passwordconfirm = self.passwordconfirm_entry.get()
        name = self.name_entry.get()
        home = self.home_entry.get()
        phone = self.phone_entry.get()
        #verify if correct
        if username == "" or password == "" or passwordconfirm == "" or name == "" or home == "" or phone == "":
            error_msg = "Form incomplete -- fill out all fields!"
        elif password != passwordconfirm:
            error_msg = "Passwords do not match!"
        ##More requirements?
        else:
            #check if an existing user already exists with this username (should probably do this in a seperate class dedicated to managing database entries)
            userExists = False
            with open('accounts.csv', 'r', newline='') as accountFile:
                reader = csv.reader(accountFile)
                for row in reader:
                    if username == row[0]:
                        error_msg = f"{username} already has an account! Are you trying to log in?"
                        userExists = True
            if userExists == False:
                error_msg = ""
                with open('accounts.csv', 'a', newline='', encoding='utf-8') as accountFile:
                    writer = csv.writer(accountFile)
                    row = [username, password, name, home, phone]
                    writer.writerow(row)
                #go back to login on successful account creation
                controller.show_frame(LogIn.main)
        self.error_label.config(text=error_msg)

    def btn_back(self, controller):
        print("back")
        #clear all fields to protect privacy
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
        self.passwordconfirm_entry.delete(0, 'end')
        self.name_entry.delete(0, 'end')
        self.home_entry.delete(0, 'end')
        self.phone_entry.delete(0, 'end')
        self.error_label.config(text="")
        controller.show_frame(LogIn.main)
        
