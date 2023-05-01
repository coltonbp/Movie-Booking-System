import tkinter as tk
from tkinter import *
import csv

class main:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Report Window")

        # Create widgets for displaying sales report
        sales_frame = tk.Frame(self.parent)
        sales_frame.pack(side=tk.LEFT, padx=5, pady=5)
        sales_label = tk.Label(sales_frame, text="Sales \n (User, Confirmation Code, Amount)")
        sales_label.pack()
        self.sales_text = tk.Text(sales_frame, height=30, width=48)
        self.sales_text.pack(padx=5, pady=5)

        # Load data from CSV file for sales report
        try:
            with open('report.csv', 'r', newline='', encoding='utf-8') as report_file:
                reader = csv.reader(report_file)
                for row in reader:
                    self.sales_text.insert(tk.END, row[0] + '  ' + row[1] + '  ' + row[2] + '\n')
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "Report file not found.")

        # Create widgets for displaying movies report
        movies_frame = tk.Frame(self.parent)
        movies_frame.pack(side=tk.RIGHT, padx=5, pady=5)
        movies_label = tk.Label(movies_frame, text="Movies\n (Movie Name, Movie Times)")
        movies_label.pack()
        self.movies_text = tk.Text(movies_frame, height=30, width=48)
        self.movies_text.pack(padx=5, pady=5)

        # Load data from CSV file for movies report
        try:
            with open('shows.csv', 'r', newline='', encoding='utf-8') as shows_file:
                reader = csv.reader(shows_file)
                for row in reader:
                    self.movies_text.insert(tk.END, row[0] + '  ' + row[3]+ '\n')
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "Shows file not found.")
      
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = main(root)
    root.mainloop()
