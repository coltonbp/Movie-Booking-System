import tkinter as tk
from tkinter import messagebox
from tkinter import Spinbox
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
        conf_num = str(random.randint(100000, 999999))
        
        # open new window to show ticket number
        new_window = tk.Toplevel(self.parent)
        new_window.title("Thank You")
        new_window.geometry("400x400")
        ticket_label = tk.Label(new_window, text="Your conformation number is: " + conf_num, font=("Helvetica", 16))
        ticket_label.pack(pady=20)
        

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x800")
    app = PurchaseWindow(root)
    root.mainloop()