import tkinter as tk
from tkinter import messagebox

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
        
        # Create purchase button
        self.purchase_button = tk.Button(self.parent, text="Purchase", command=self.purchase)
        self.purchase_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        
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
        new_window = tk.Toplevel(self.parent)
        new_window.title("Thank You")
        new_window.geometry("400x400")
        image_label = tk.Label(new_window, text="Thank you for your purchase!", font=("Helvetica", 16))
        image_label.pack(pady=20)
        default_image = tk.PhotoImage(file="default_image.png")
        image_widget = tk.Label(new_window, image=default_image)
        image_widget.image = default_image # keep reference to image to avoid garbage collection
        image_widget.pack(pady=20)
        

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x800")
    app = PurchaseWindow(root)
    root.mainloop()
