import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import hashlib

# Application window for master password input
root = tk.Tk()
root.title("Your Password Manager")
root.geometry("300x200")

label = ttk.Label(root, text="Type in your master password:")
label.pack(pady=10)

password_entry = ttk.Entry(root, show="*")
password_entry.pack(pady=10)

def submit_password():
    master_password = password_entry.get()
    if check_master_password(master_password):
        open_main_window()
        root.withdraw()
    else:
        messagebox.showerror("Error", "Incorrect password")

def check_master_password(string) -> bool:
    return string == "1234"

submit_button = ttk.Button(root, text="Submit", command=submit_password)
submit_button.pack(pady=10)

# Function to open the main application window
def open_main_window():
    main_window = tk.Toplevel(root)
    main_window.title("Password Manager")
    main_window.geometry("500x400")

    top_frame = ttk.Frame(main_window)
    top_frame.pack(pady=10)

    middle_frame = ttk.Frame(main_window)
    middle_frame.pack(pady=10)

    bottom_frame = ttk.Frame(main_window)
    bottom_frame.pack(pady=10)

    ttk.Label(top_frame, text="Your Passwords:", font=("Arial", 14)).pack()

root.mainloop()