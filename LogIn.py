import tkinter as tk
from tkinter import ttk
import csv
import fetch as db
import CreateAcc
import ViewCatalog

Header1 = ("Helvetica", 25)
Header2 = ("Helvetica", 16)
LargeText = ("Helvetica", 14)
adminUser='admin'
adminPass='adminpass'
username = 'defaultuser'
isAdmin = False

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

        # Welcome label
        self.welcome_label = tk.Label(self, text="Welcome, Please Login or Register", font=Header2)
        self.welcome_label.grid(row=1, column=1)

        # Error message label
        self.error_label = tk.Label(self, text="", fg="red")
        self.error_label.grid(row=2, column=1)

        # Username label and entry
        self.username_label = tk.Label(self, text="Email")
        self.username_label.grid(row=3, column=1)
        self.username_entry = tk.Entry(self, width=30)
        self.username_entry.grid(row=4, column=1)

        # Password label and entry
        self.password_label = tk.Label(self, text="Password")
        self.password_label.grid(row=5, column=1)
        self.password_entry = tk.Entry(self, width=30, show="*")
        self.password_entry.grid(row=6, column=1)

        # Log in button
        self.login_button = tk.Button(self, text="Log In", width=30, command=lambda: self.btn_login(controller))
        self.login_button.grid(row=7, column=1)

        # Account prompt label
        self.accountPrompt_label = tk.Label(self, text="Don't have an account?")
        self.accountPrompt_label.grid(row=8, column=1)

        # Create account button
        self.create_button = tk.Button(self, text="Create Account", width=30, command=lambda: self.btn_create(controller))
        self.create_button.grid(row=9, column=1)

    def newLogin(self, controller, username, isAdmin):
        self.username = username
        self.isAdmin = isAdmin
        name = db.readFrom("accounts", username, "name")
        print("New Login: " + self.username + " (" + str(name) + "), isAdmin: " + str(self.isAdmin))
        info = [username, isAdmin, name]
        db.writeTo("currentLogin", [info], 'w')
        ViewCatalog.main.refresh(self)

    def resetForm(self):
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
        self.error_label.config(text="")
    
    def btn_login(self, controller):
        #get data from entry fields
        username = self.username_entry.get()
        password = self.password_entry.get()
        #verify if correct (should probably do this in a seperate class dedicated to managing database entries)
        verified = False
        admin = False
        if username == adminUser and password == adminPass:
            verified = True
            admin = True
            error_msg = ""
            self.resetForm()
            self.newLogin(controller, username, True)
            controller.show_frame(ViewCatalog.main)
        else:
            try:
                with open('accounts.csv', 'r', newline='') as accountFile:
                    reader = csv.reader(accountFile)
                    for row in reader:
                        if username == row[0] and password == row[1]:
                            verified = True
                            break
            except FileNotFoundError:
                #file may not exist yet if there have been no accounts created.
                pass
                        
            if verified == True:
                error_msg = ""
                #clear all fields to protect privacy
                self.resetForm()
                self.newLogin(controller, username, False)
                controller.show_frame(ViewCatalog.main)
            else:
                error_msg = "Username and/or password are incorrect or do not exist."
        self.error_label.config(text=error_msg)

    def btn_create(self, controller):
        #clear all fields to protect privacy
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
        self.error_label.config(text="")
        controller.show_frame(CreateAcc.main)
