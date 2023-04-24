import tkinter as tk
import tkinter.messagebox


class LogOnGUI:
    def __init__(self, root):
        self.root = root
        self.loginv = 0

        # Welcome label
        welcome_label = tk.Label(self.root, text="Welcome", font=("Helvetica", 16))
        welcome_label.grid(row=0, column=0, columnspan=2)

        # Log in button
        login_button = tk.Button(self.root, text="Log in", command=self.log_in)
        login_button.grid(row=1, column=0)

        # Create account button
        create_button = tk.Button(self.root, text="Create account", command=self.create_account)
        create_button.grid(row=1, column=1)

        # Username label and entry
        self.username_label = tk.Label(self.root, text="Username:")
        self.username_entry = tk.Entry(self.root)

        # Password label and entry
        self.password_label = tk.Label(self.root, text="Password:")
        self.password_entry = tk.Entry(self.root, show="*")

        # Security question label and entry
        self.security_question_label = tk.Label(self.root, text="Security question:")
        self.security_question_entry = tk.Entry(self.root)

    def log_in(self):
        # Hide create account widgets
        self.username_label.grid_remove()
        self.username_entry.grid_remove()
        self.password_label.grid_remove()
        self.password_entry.grid_remove()
        self.security_question_label.grid_remove()
        self.security_question_entry.grid_remove()

        # Show log in widgets
        self.username_label.grid(row=2, column=0)
        self.username_entry.grid(row=2, column=1)
        self.password_label.grid(row=3, column=0)
        self.password_entry.grid(row=3, column=1)

        # Submit button
        submit_button = tk.Button(self.root, text="Submit", command=lambda: self.log_in_submit())
        submit_button.grid(row=4, column=1)

    def log_in_submit(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "Student" and password == "Tech":
            # Show security question widgets
            self.security_question_label.grid(row=5, column=0)
            self.security_question_entry.grid(row=5, column=1)

            # Submit button
            submit_button = tk.Button(self.root, text="Submit", command=lambda: self.security_question_submit())
            submit_button.grid(row=6, column=1)

        else:
            # Display authentication failed message
            message_label = tk.Label(self.root, text="Authentication Failed")
            message_label.grid(row=4, column=0)

    def security_question_submit(self):
        security_question = self.security_question_entry.get()

        if security_question == "Lubbock":
            # Display welcome message
            message_label = tk.Label(self.root, text="Welcome")
            message_label.grid(row=7, column=0, columnspan=2)

            self.loginv = 1  # this will help with the preconditions of the next classes
        else:
            # Display wrong answer message
            message_label = tk.Label(self.root, text="Wrong answer")
            message_label.grid(row=6, column=0)

   

    def create_account(self):
        # Hide log in widgets
        self.username_label.grid_remove()
        self.username_entry.grid_remove()
        self.password_label.grid_remove()
        self.password_entry.grid_remove()
        self.security_question_label.grid_remove()
        self.security_question_entry.grid_remove()

        # Show create account widgets
        id_label = tk.Label(self.root, text="ID:")
        id_entry = tk.Entry(self.root)

        email_label = tk.Label(self.root, text="Email:")
        email_entry = tk.Entry(self.root)

        name_label = tk.Label(self.root, text="Name:")
        name_entry = tk.Entry(self.root)

        username_label = tk.Label(self.root, text="Username:")
        username_entry = tk.Entry(self.root)

        password_label = tk.Label(self.root, text="Password:")
        password_entry = tk.Entry(self.root, show="*")

        # Submit button
        submit_button = tk.Button(self.root, text="Submit", command=lambda: self.create_account_submit(
            id_entry.get(),
            email_entry.get(),
            name_entry.get(),
            username_entry.get(),
            password_entry.get(),
        ))
        submit_button.grid(row=6, column=1)

        id_label.grid(row=2, column=0)
        id_entry.grid(row=2, column=1)

        email_label.grid(row=3, column=0)
        email_entry.grid(row=3, column=1)

        name_label.grid(row=4, column=0)
        name_entry.grid(row=4, column=1)

        username_label.grid(row=5, column=0)
        username_entry.grid(row=5, column=1)

        password_label.grid(row=6, column=0)
        password_entry.grid(row=6, column=1)

    def create_account_submit(self, id_entry, email_entry, name_entry, username_entry, password_entry):
        id_num = id_entry.get()
        email = email_entry.get()
        name = name_entry.get()
        username = username_entry.get()
        password = password_entry.get()

        # Store account information in a file
        with open("accounts.txt", "a") as f:
            f.write(f"{id_num},{email},{name},{username},{password}\n")

        # Display confirmation message
        message_label = tk.Label(self.root, text="Account created!")
        message_label.grid(row=7, column=0)

    def go_to_main_menu(self, destroy, ):
        self.root.destroy()
        MainGUI(self.loginv)

class MainGUI:
    def __init__(self, loginv):
        self.loginv = loginv
        self.root = tk.Tk()
        self.root.title("Main Menu")

        # Welcome label
        welcome_label = tk.Label(self.root, text="Welcome!", font=("Helvetica", 16))
        welcome_label.pack()

        # Account information button
        account_button = tk.Button(self.root, text="Account Information", command=self.account_info)
        account_button.pack()

        # Log out button
        logout_button = tk.Button(self.root, text="Log Out", command=self.log_out)
        logout_button.pack()

        self.root.mainloop()

    def account_info(self):
        # Display account information
        with open("accounts.txt", "r") as f:
            for line in f:
                if line.startswith(str(self.loginv)):
                    account_info = line.split(",")
                    message_label = tk.Label(self.root, text=f"Username: {account_info[1]}\nPassword: {account_info[2]}\nSecurity Question: {account_info[3]}")
                    message_label.pack()

    def log_out(self):
        self.root.destroy()

    def showinfo(self,inf): # indent these:
        self.value.set(inf)
        LogOnGUI(tk.Tk())

if __name__ == "__main__":
    LogOnGUI(tk.Tk())
