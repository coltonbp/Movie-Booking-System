import tkinter as tk
from tkinter import messagebox
from tkinter import Spinbox
import csv
import random

class PurchaseWindow:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Purchase Window")
        
        # Create widgets for credit card payment
        self.cc_label = tk.Label(self.parent, text="Credit Card Number:")
        self.cc_entry = tk.Entry(self.parent, show="*")
        self.cc_label.grid(row=0, column=0, padx=5, pady=5)
        self.cc_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Create widgets for PayPal payment
        self.pp_label = tk.Label(self.parent, text="PayPal Account:")
        self.pp_entry = tk.Entry(self.parent)
        self.pp_label.grid(row=1, column=0, padx=5, pady=5)
        self.pp_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Create widgets for selecting number of tickets
        self.tickets_label = tk.Label(self.parent, text="Number of Tickets:")
        self.tickets_spinbox = tk.Spinbox(self.parent, from_=1, to=10)
        self.tickets_label.grid(row=2, column=0, padx=5, pady=5)
        self.tickets_spinbox.grid(row=2, column=1, padx=5, pady=5)
        
        # Create purchase button
        self.purchase_button = tk.Button(self.parent, text="Purchase", command=self.purchase)
        self.purchase_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
    def purchase(self):
        # Check if either credit card or PayPal information is filled out
        if not self.cc_entry.get() and not self.pp_entry.get():
            messagebox.showerror("Error", "Please enter credit card information or PayPal account.")
            return
        
        # Process payment based on information provided
        if self.cc_entry.get():
            # Process credit card payment
            messagebox.showinfo("Success", "Credit card payment processed successfully.")
        else:
            # Process PayPal payment
            messagebox.showinfo("Success", "PayPal payment processed successfully.")
        
        # Clear entries
        self.cc_entry.delete(0, tk.END)
        self.pp_entry.delete(0, tk.END)
        
        # Create new window with default image
        bar_c = str(random.randint(100000, 999999))
        num_tickets = int(self.tickets_spinbox.get())
        
        # open new window to show ticket number
        new_window = tk.Toplevel(self.parent)
        new_window.title("Thank You")
        new_window.geometry("400x400")
        barc_mess = tk.Label(new_window, text="Your confirmation number is: " + bar_c, font=("Helvetica", 16))
        barc_mess.pack(pady=20)
        
        filename="currentLogin.csv"
        
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == str(True):
                    usern=row[0]
            else:
                print("No match found.")
        try:
            with open('report.csv', 'a', newline='', encoding='utf-8') as accountFile:
                writer = csv.writer(accountFile)
                row = [usern,bar_c,num_tickets]
                writer.writerow(row)
        except PermissionError:
            error_msg = "An error occurred due to file access permission being denied."
            self.error_label.config(text=error_msg)
            return


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x800")
    app = PurchaseWindow(root)
    root.mainloop()