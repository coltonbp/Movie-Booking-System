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

        # Create widgets for displaying sales report
        sales_frame = tk.Frame(self)
        sales_frame.pack(side=tk.LEFT, padx=5, pady=5)
        sales_label = tk.Label(sales_frame, text="Sales \n (User, Confirmation Code, Amount, Show)")
        sales_label.pack()
        self.sales_text = tk.Text(sales_frame, height=30, width=48)
        self.sales_text.pack(padx=5, pady=5)

        # Create widgets for displaying movies report
        movies_frame = tk.Frame(self)
        movies_frame.pack(side=tk.RIGHT, padx=5, pady=5)
        movies_label = tk.Label(movies_frame, text="Movies\n (Movie Name, Movie Times)")
        movies_label.pack()
        self.movies_text = tk.Text(movies_frame, height=30, width=48)
        self.movies_text.pack(padx=5, pady=5)

        # Back button
        self.back_button = tk.Button(self, text="<-- Go Back", width=10, command=lambda: self.btn_back(controller))
        self.back_button.pack(padx=5, pady=5)

    def refresh(self=thisSelf):
        global thisSelf
        self = thisSelf
        self.sales_text.delete("1.0", "end-1c")
        self.movies_text.delete("1.0", "end-1c")
        self.getSales()
        self.getMovies()

    def getMovies(self):
        # Load data from CSV file for movies report
        try:
            with open('shows.csv', 'r', newline='', encoding='utf-8') as shows_file:
                reader = csv.reader(shows_file)
                for row in reader:
                    self.movies_text.insert(tk.END, row[0] + '  ' + row[3]+ '\n')
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "Shows file not found.")
            
    def getSales(self):
        # Load data from CSV file for sales report
        try:
            with open('tickets.csv', 'r', newline='', encoding='utf-8') as report_file:
                reader = csv.reader(report_file)
                for row in reader:
                    self.sales_text.insert(tk.END, row[1] + '  ' + row[4] + '  ' + row[5] + '  ' + row[2] + '\n')
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "Ticket file not found.")

    def btn_back(self, controller):
        ViewCatalog.main.refresh()
        controller.show_frame(ViewCatalog.main)
        
