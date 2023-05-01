import tkinter as tk
from tkinter import ttk
import csv
import random
import fetch as db
import LogIn
import ManageShows
import LeaveReview
import BookTicket
import ViewReport
import ViewTickets

Header1 = ("Helvetica", 25)
Header2 = ("Helvetica", 16)
LargeText = ("Helvetica", 14)

#placeholders
username='defaultuser'
name='User'

isAdmin=False
catalogScroll=0
currentSearchTerm=''
thisSelf=None

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

        #scroll up button
        self.scrUp_button = tk.Button(self, text="↑", bg='darkgray', font=LargeText, command=lambda: self.btn_scroll("Up"))
        self.scrUp_button.grid(row=2, column=0, columnspan=4, sticky="nsew")

        #TODO: Populate shows
        #placeholder
        #show title
        self.show1Title_label = tk.Label(self, text='', font=Header1, bg='lightgray')
        self.show2Title_label = tk.Label(self, text='', font=Header1, bg='lightgray')
        self.show3Title_label = tk.Label(self, text='', font=Header1, bg='lightgray')
        self.show1Title_label.grid(row=3, column=0, sticky="nsew")
        self.show2Title_label.grid(row=6, column=0, sticky="nsew")
        self.show3Title_label.grid(row=9, column=0, sticky="nsew")

        #show times
        #timesStr = ''
        #i = 0
        #for time in showTimes:
        #    if i != 0:
        #        timesStr = timesStr + ", "
        #    timesStr = timesStr + time
        #    i = i + 1
        self.show1Times_label = tk.Label(self, text='', font=Header1, bg='lightgray')
        self.show2Times_label = tk.Label(self, text='', font=Header1, bg='lightgray')
        self.show3Times_label = tk.Label(self, text='', font=Header1, bg='lightgray')
        self.show1Times_label.grid(row=3, column=1, columnspan=2, sticky="nsew")
        self.show2Times_label.grid(row=6, column=1, columnspan=2, sticky="nsew")
        self.show3Times_label.grid(row=9, column=1, columnspan=2, sticky="nsew")

        #show desc
        self.show1Desc_label = tk.Label(self, text='', bg='lightgray', font=LargeText, height=5, wraplength=300)
        self.show2Desc_label = tk.Label(self, text='', bg='lightgray', font=LargeText, height=5, wraplength=300)
        self.show3Desc_label = tk.Label(self, text='', bg='lightgray', font=LargeText, height=5, wraplength=300)
        self.show1Desc_label.grid(row=4, column=0, rowspan=2, sticky="nsew")
        self.show2Desc_label.grid(row=7, column=0, rowspan=2, sticky="nsew")
        self.show3Desc_label.grid(row=10, column=0, rowspan=2, sticky="nsew")

        #review user
        self.show1ReviewUser_label = tk.Label(self, text='', font=LargeText, anchor='w', bg='lightgray')
        self.show2ReviewUser_label = tk.Label(self, text='', font=LargeText, anchor='w', bg='lightgray')
        self.show3ReviewUser_label = tk.Label(self, text='', font=LargeText, anchor='w', bg='lightgray')
        self.show1ReviewUser_label.grid(row=4, column=1, sticky="nsew")
        self.show2ReviewUser_label.grid(row=7, column=1, sticky="nsew")
        self.show3ReviewUser_label.grid(row=10, column=1, sticky="nsew")

        #review rating
        self.show1ReviewRate_label = tk.Label(self, text='', font=LargeText, anchor='e', bg='lightgray')
        self.show2ReviewRate_label = tk.Label(self, text='', font=LargeText, anchor='e', bg='lightgray')
        self.show3ReviewRate_label = tk.Label(self, text='', font=LargeText, anchor='e', bg='lightgray')
        self.show1ReviewRate_label.grid(row=4, column=2, sticky="nsew")
        self.show2ReviewRate_label.grid(row=7, column=2, sticky="nsew")
        self.show3ReviewRate_label.grid(row=10, column=2, sticky="nsew")

        #review desc
        self.show1ReviewDesc_label = tk.Label(self, text='', font=LargeText, bg='lightgray', height=5, wraplength=200)
        self.show2ReviewDesc_label = tk.Label(self, text='', font=LargeText, bg='lightgray', height=5, wraplength=200)
        self.show3ReviewDesc_label = tk.Label(self, text='', font=LargeText, bg='lightgray', height=5, wraplength=200)
        self.show1ReviewDesc_label.grid(row=5, column=1, columnspan=2, sticky="nsew")
        self.show2ReviewDesc_label.grid(row=8, column=1, columnspan=2, sticky="nsew")
        self.show3ReviewDesc_label.grid(row=11, column=1, columnspan=2, sticky="nsew")

        #show button
        self.show1_button = tk.Button(self, text='', bg='darkgray', font=Header1, state=tk.DISABLED, command=lambda: self.btn_bookTickets(controller, isAdmin, 0))
        self.show2_button = tk.Button(self, text='', bg='darkgray', font=Header1, state=tk.DISABLED, command=lambda: self.btn_bookTickets(controller, isAdmin, 1))
        self.show3_button = tk.Button(self, text='', bg='darkgray', font=Header1, state=tk.DISABLED, command=lambda: self.btn_bookTickets(controller, isAdmin, 2))
        self.show1_button.grid(row=3, column=3, rowspan=3, sticky="nsew")
        self.show2_button.grid(row=6, column=3, rowspan=3, sticky="nsew")
        self.show3_button.grid(row=9, column=3, rowspan=3, sticky="nsew")

        #scroll down button
        self.scrDown_button = tk.Button(self, text="↓", bg='darkgray', font=LargeText, command=lambda: self.btn_scroll("Down"))
        self.scrDown_button.grid(row=12, column=0, columnspan=4, sticky="nsew")

        #view tickets button
        self.viewTickets_button = tk.Button(self, text="View Your Tickets", bg='darkgray', font=Header2, command=lambda: self.btn_viewTickets(controller, isAdmin))
        self.viewTickets_button.grid(row=13, column=0, sticky="sew")

        #review movie button
        self.reviewMovie_button = tk.Button(self, text="Review a Movie", bg='darkgray', font=Header2, command=lambda: self.btn_reviewMovie(controller, isAdmin))
        self.reviewMovie_button.grid(row=13, column=1, columnspan=2, sticky="sew")

        #log out button
        self.LogOut_button = tk.Button(self, text="Log Out", bg='darkgray', font=Header2, command=lambda: self.btn_logOut(controller))
        self.LogOut_button.grid(row=13, column=3, sticky="sew")

        self.rowconfigure(13, weight=1)
        
        global thisSelf
        thisSelf = self
        
    def refresh(self=thisSelf, searchterm=''):
        global thisSelf
        global isAdmin
        print("refresh listings with term: '"+searchterm+"'")
        self = thisSelf

        isAdmin = (db.readFrom('currentLogin', '', 'admin') == "True")
        #update login
        if isAdmin:
            viewTicketsTxt = "View Report"
            reviewBtnTxt = "Manage Shows"
            bookTicketsTxt = "Edit Show"
        else:
            viewTicketsTxt = "View Tickets"
            reviewBtnTxt = "Review a Show"
            bookTicketsTxt = "Book Tickets"
        self.viewTickets_button.config(text=viewTicketsTxt)
        self.reviewMovie_button.config(text=reviewBtnTxt)
        self.show1_button.config(text=bookTicketsTxt)
        self.show2_button.config(text=bookTicketsTxt)
        self.show3_button.config(text=bookTicketsTxt)

        if isAdmin:
            name = "Admin"
        else:
            name = db.readFrom('currentLogin', '', 'name')
        self.welcome_label.config(text=f"Welcome, {name}")

        #refresh listings
##        showTimes = ['12:00p', '2:30p', '5:30p', '9:00p']
##        showDesc = "This very cool movie is bound to knock your socks off! Starring John Johnson and Jane Jackson, Directed by Don Donaldson."
##        reviewUser = "Movie_Lover"
##        reviewRate = 1
##        reviewDesc = "Despite what you might think, this movie is, in fact, not cool at all."
        shows = db.searchFor('shows', searchterm)
        reviews = []
        i = 0
        while i < 3:
            j = catalogScroll + i
            if j < len(shows):
                if i == 0:
                    self.show1Title_label.config(text=shows[j][0])
                    self.show1Desc_label.config(text=shows[j][2])
                    self.show1Times_label.config(text=shows[j][3])
                    reviews = db.readFrom('reviews', shows[j][0], '', True)
                    if len(reviews) > 0:
                        r = random.randrange(len(reviews))
                        self.show1ReviewUser_label.config(text=reviews[r][1])
                        self.show1ReviewDesc_label.config(text=reviews[r][3])
                        self.show1ReviewRate_label.config(text=str(reviews[r][2]) + "/5 Stars")
                    else:
                        self.show1ReviewUser_label.config(text='')
                        self.show1ReviewDesc_label.config(text='')
                        self.show1ReviewRate_label.config(text='')
                    
                    if shows[j][1] == "1" or isAdmin:
                        self.show1_button.config(state=tk.NORMAL)
                    else:
                        self.show1_button.config(state=tk.DISABLED)
                elif i == 1:
                    self.show2Title_label.config(text=shows[j][0])
                    self.show2Desc_label.config(text=shows[j][2])
                    self.show2Times_label.config(text=shows[j][3])
                    reviews = db.readFrom('reviews', shows[j][0], '', True)
                    if len(reviews) > 0:
                        r = random.randrange(len(reviews))
                        self.show2ReviewUser_label.config(text=reviews[r][1])
                        self.show2ReviewDesc_label.config(text=reviews[r][3])
                        self.show2ReviewRate_label.config(text=str(reviews[r][2]) + "/5 Stars")
                    else:
                        self.show2ReviewUser_label.config(text='')
                        self.show2ReviewDesc_label.config(text='')
                        self.show2ReviewRate_label.config(text='')
                    if shows[j][1] == "1" or isAdmin:
                        self.show2_button.config(state=tk.NORMAL)
                    else:
                        self.show2_button.config(state=tk.DISABLED)
                    
                elif i == 2:
                    self.show3Title_label.config(text=shows[j][0])
                    self.show3Desc_label.config(text=shows[j][2])
                    self.show3Times_label.config(text=shows[j][3])
                    reviews = db.readFrom('reviews', shows[j][0], '', True)
                    if len(reviews) > 0:
                        r = random.randrange(len(reviews))
                        self.show3ReviewUser_label.config(text=reviews[r][1])
                        self.show3ReviewDesc_label.config(text=reviews[r][3])
                        self.show3ReviewRate_label.config(text=str(reviews[r][2]) + "/5 Stars")
                    else:
                        self.show3ReviewUser_label.config(text='')
                        self.show3ReviewDesc_label.config(text='')
                        self.show3ReviewRate_label.config(text='')
                    if shows[j][1] == "1" or isAdmin:
                        self.show3_button.config(state=tk.NORMAL)
                    else:
                        self.show3_button.config(state=tk.DISABLED)
            else:
                if i == 0:
                    self.show1Title_label.config(text="")
                    self.show1Desc_label.config(text="")
                    self.show1Times_label.config(text="")
                    self.show1_button.config(state=tk.DISABLED)
                elif i == 1:
                    self.show2Title_label.config(text="")
                    self.show2Desc_label.config(text="")
                    self.show2Times_label.config(text="")
                    self.show2_button.config(state=tk.DISABLED)
                elif i == 2:
                    self.show3Title_label.config(text="")
                    self.show3Desc_label.config(text="")
                    self.show3Times_label.config(text="")
                    self.show3_button.config(state=tk.DISABLED)
            i = i + 1

    def searchFocus(self):
        self.search_entry.delete(0, 'end')
        self.search_entry.configure(fg='black')

    def resetSearch(self, searchBox):
        searchBox.delete(0, 'end')
        searchBox.insert(0, "Search Shows")
        searchBox.configure(fg='gray')
        
    def btn_search(self):
        global currentSearchTerm
        global catalogScroll
        searchTerm = self.search_entry.get()
        catalogScroll = 0
        self.refresh(searchTerm)
        currentSearchTerm = searchTerm

    def btn_scroll(self, direction):
        global catalogScroll
        global currentSearchTerm
        if direction.lower() == "up":
            if catalogScroll > 0:
                catalogScroll = catalogScroll - 1
        elif direction.lower() == "down":
            if catalogScroll + 3 < len(db.searchFor('shows', currentSearchTerm)):
                catalogScroll = catalogScroll + 1
        self.refresh(currentSearchTerm)

    def btn_viewTickets(self, controller, isAdmin):
        if isAdmin:
            ViewReport.main.refresh()
            controller.show_frame(ViewReport.main)
        else:
            ViewTickets.main.refresh()
            controller.show_frame(ViewTickets.main)

    def btn_reviewMovie(self, controller, isAdmin):
        self.resetSearch(self.search_entry)
        global catalogScroll
        catalogScroll = 0
        if isAdmin:
            ManageShows.main.refresh()
            controller.show_frame(ManageShows.main)
        else:
            LeaveReview.main.refresh()
            controller.show_frame(LeaveReview.main)

    def btn_bookTickets(self, controller, isAdmin, btnId):
        if isAdmin:
            if btnId == 0:
                print("Edit " + self.show1Title_label["text"])
                self.btn_reviewMovie(controller, isAdmin)
                ManageShows.main.selectShow(self, self.show1Title_label["text"])
            elif btnId == 1:
                print("Edit " + self.show2Title_label["text"])
                self.btn_reviewMovie(controller, isAdmin)
                ManageShows.main.selectShow(self, self.show2Title_label["text"])
            elif btnId == 2:
                print("Edit " + self.show3Title_label["text"])
                self.btn_reviewMovie(controller, isAdmin)
                ManageShows.main.selectShow(self, self.show3Title_label["text"])
        else:
            if btnId == 0:
                BookTicket.main.initShow(self, self.show1Title_label["text"])
                BookTicket.main.refresh(self)
                controller.show_frame(BookTicket.main)
            elif btnId == 1:
                BookTicket.main.initShow(self, self.show2Title_label["text"])
                BookTicket.main.refresh(self)
                controller.show_frame(BookTicket.main)
            elif btnId == 2:
                BookTicket.main.initShow(self, self.show3Title_label["text"])
                BookTicket.main.refresh(self)
                controller.show_frame(BookTicket.main)

    def btn_logOut(self, controller):
        print("Log Out")
        self.resetSearch(self.search_entry)
        global catalogScroll
        catalogScroll = 0
        controller.show_frame(LogIn.main)
