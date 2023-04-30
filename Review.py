import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Movie Booking System")

rating_scale = ttk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL)
rating_scale.grid(column=1, row=1, padx=5, pady=5)

def about_window():
    window = tk.Toplevel()
    window.title("About Movie Booking System")
    window.geometry("300x100")
    label = ttk.Label(window, text="This program was developed by John Doe.")
    label.pack(padx=5, pady=5)
    close_button = ttk.Button(window, text="Close", command=window.destroy)
    close_button.pack(padx=5, pady=5)

def submit_review():
    movie_title = movie_entry.get()
    review_text = review_text.get("1.0", tk.END)
    rating = rating_scale.get()
    # TODO: Add code to submit the review

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about_window)
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)
root.config(menu=menu_bar)

movie_label = ttk.Label(root, text="Enter movie name:")
movie_entry = ttk.Entry(root)
rating_label = ttk.Label(root, text="Enter rating (1-10):")
rating_scale = ttk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL)
review_label = ttk.Label(root, text="Enter review:")
review_text = tk.Text(root, width=40, height=10)
submit_button = ttk.Button(root, text="Submit", command=submit_review)

movie_label.grid(column=0, row=0, padx=5, pady=5)
movie_entry.grid(column=1, row=0, padx=5, pady=5)
rating_label.grid(column=0, row=1, padx=5, pady=5)
rating_scale.grid(column=1, row=1, padx=5, pady=5)
review_label.grid(column=0, row=2, padx=5, pady=5)
review_text.grid(column=1, row=2, padx=5, pady=5)
submit_button.grid(column=0, row=3, columnspan=2, padx=5, pady=5)

root.mainloop()