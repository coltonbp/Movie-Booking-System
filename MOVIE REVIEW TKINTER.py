import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Movie Booking System")

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
rating_entry = ttk.Entry(root)
review_label = ttk.Label(root, text="Enter review:")
review_text = tk.Text(root, width=40, height=10)
submit_button = ttk.Button(root, text="Submit", command=submit_review)

movie_label.grid(column=0, row=0, padx=5, pady=5)
movie_entry.grid(column=1, row=0, padx=5, pady=5)
rating_label.grid(column=0, row=1, padx=5, pady=5)
rating_entry.grid(column=1, row=1, padx=5, pady=5)
review_label.grid(column=0, row=2, padx=5, pady=5)
review_text.grid(column=1, row=2, padx=5, pady=5)
submit_button.grid(column=0, row=3, columnspan=2, padx=5, pady=5)

def submit_review():
    movie = Movie(movie_entry.get(), "")
    review = Review(movie, review_text.get("1.0", "end-1c"), int(rating_entry.get()))
    create_review(movies, movie, review.get_review_text(), review.get_rating())
    movie_entry.delete(0, tk.END)
    rating_entry.delete(0, tk.END)
    review_text.delete("1.0", tk.END)
    messagebox.showinfo("Review Submitted", "Review added successfully!")

root.mainloop()
