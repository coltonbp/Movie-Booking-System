import tkinter as tk
from tkinter import *
import csv


class main:

    def __init__(self, parent):
        self.parent = parent
        self.parent.title("View Tickets")

        # Create widgets for displaying sales report
        sales_frame = tk.Frame(self.parent)
        sales_frame.pack(padx=100, pady=100)
        sales_label = tk.Label(sales_frame, text="Your Tickets \n ()")
        sales_label.pack()
        self.tickets_text = tk.Text(sales_frame, height=30, width=48)
        self.tickets_text.pack(padx=5, pady=5)
        filename = "currentLogin.csv"
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                usern=row[0]
        try:
            with open('report.csv', 'r', newline='', encoding='utf-8') as report_file:
                    reader = csv.reader(report_file)
                    if row[0]==usern:
                        for row in reader:
                            self.tickets_text.insert(tk.END, row[0] + '  ' + row[1] + '  ' + row[2] + '\n')
        except FileNotFoundError:
                tk.messagebox.showerror("Error", "Report file not found.")
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = main(root)
    root.mainloop()