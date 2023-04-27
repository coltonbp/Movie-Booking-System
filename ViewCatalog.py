import tkinter as tk
from tkinter import ttk
import csv
import LogIn

Header1 = ("Helvetica", 25)
Header2 = ("Helvetica", 16)
LargeText = ("Helvetica", 14)

#placeholders
username='defaultuser'
name='User'
showTimes = ['12:00p', '2:30p', '5:30p', '9:00p']
showDesc = "This very cool movie is bound to knock your socks off! Starring John Johnson and Jane Jackson, Directed by Don Donaldson."
reviewUser = "Movie_Lover"
reviewRate = 1
reviewDesc = "Despite what you might think, this movie is, in fact, not cool at all."

class main(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #column and row config
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=3)

        # Title label
        self.title_label = tk.Label(self, text="West TX Movie Booking System", font=Header2, anchor='e')
        self.title_label.grid(row=0, column=1, columnspan=3, sticky="e")

        # Welcome label
        self.welcome_label = tk.Label(self, text=f"Welcome, {name}.", font=Header2, anchor='w')
        self.welcome_label.grid(row=0, column=0, sticky="w")

        #Catalog label
        self.catalog_label = tk.Label(self, text="Catalog", font=Header1, anchor='w')
        self.catalog_label.grid(row=1, column=0, sticky="w")

        #Search bar entry
        self.search_entry = tk.Entry(self, width=60, fg='gray')
        self.search_entry.insert(0, "Search Shows")
        self.search_entry.bind("<FocusIn>", lambda x: self.searchFocus())
        self.search_entry.grid(row=1, column=1, columnspan=2, sticky="nsew")

        #search bar button
        self.search_button = tk.Button(self, text="Search", bg='darkgray', font=LargeText, command=lambda: self.btn_search())
        self.search_button.grid(row=1, column=3, sticky="nsew")

        #TODO: Populate shows
        #placeholder
        #show title
        self.showTitle_label = tk.Label(self, text="Very Cool Movie", font=Header1, bg='lightgray')
        self.showTitle_label.grid(row=2, column=0, sticky="nsew")

        #show times
        timesStr = ''
        i = 0
        for time in showTimes:
            if i != 0:
                timesStr = timesStr + ", "
            timesStr = timesStr + time
            i = i + 1
        self.showTimes_label = tk.Label(self, text=timesStr, font=Header1, bg='lightgray')
        self.showTimes_label.grid(row=2, column=1, columnspan=2, sticky="nsew")

        #show desc
        self.showDesc_label = tk.Label(self, text=showDesc, bg='lightgray', font=LargeText, height=5, wraplength=300)
        self.showDesc_label.grid(row=3, column=0, rowspan=2, sticky="nsew")

        #review user
        self.showReviewUser_label = tk.Label(self, text=reviewUser, font=LargeText, anchor='w', bg='lightgray')
        self.showReviewUser_label.grid(row=3, column=1, sticky="nsew")

        #review rating
        self.showReviewRate_label = tk.Label(self, text=f"{reviewRate}/5 Stars", font=LargeText, anchor='e', bg='lightgray')
        self.showReviewRate_label.grid(row=3, column=2, sticky="nsew")

        #review desc
        self.showReviewDesc_label = tk.Label(self, text=reviewDesc, font=LargeText, bg='lightgray', height=5, wraplength=200)
        self.showReviewDesc_label.grid(row=4, column=1, columnspan=2, sticky="nsew")

        #show button
        self.show_button = tk.Button(self, text="Book Tickets", bg='darkgray', font=Header1, command=lambda: self.btn_bookTickets(controller))
        self.show_button.grid(row=2, column=3, rowspan=3, sticky="nsew")

        #view tickets button
        self.viewTickets_button = tk.Button(self, text="View Your Tickets", bg='darkgray', font=Header2, command=lambda: self.btn_viewTickets(controller))
        self.viewTickets_button.grid(row=5, column=0, sticky="sew")

        #review movie button
        self.reviewMovie_button = tk.Button(self, text="Review a Movie", bg='darkgray', font=Header2, command=lambda: self.btn_reviewMovie(controller))
        self.reviewMovie_button.grid(row=5, column=1, columnspan=2, sticky="sew")

        #log out button
        self.LogOut_button = tk.Button(self, text="Log Out", bg='darkgray', font=Header2, command=lambda: self.btn_logOut(controller))
        self.LogOut_button.grid(row=5, column=3, sticky="sew")

    def searchFocus(self):
        self.search_entry.delete(0, 'end')
        self.search_entry.configure(fg='black')

    def resetSearch(self, searchBox):
        searchBox.delete(0, 'end')
        searchBox.insert(0, "Search Shows")
        searchBox.configure(fg='gray')
        
    def btn_search(self):
        print("Search")

    def btn_viewTickets(self, controller):
        print("View Tickets")

    def btn_reviewMovie(self, controller):
        print("Review Movie")

    def btn_logOut(self, controller):
        print("Log Out")
        self.resetSearch(self.search_entry)
        controller.show_frame(LogIn.main)

    def btn_bookTickets(self, controller):
        print("Book tickets")
