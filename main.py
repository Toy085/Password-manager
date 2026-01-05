import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Your Password Manager")
root.geometry("500x400")

# Label
label = ttk.Label(root, text="Type in your master password:")
label.pack(pady=10)

password_entry = ttk.Entry(root, show="*")
password_entry.pack(pady=10)

def submit_password():
    master_password = password_entry.get()
    print(f"Password Entered: {master_password}")

submit_button = ttk.Button(root, text="Submit", command=submit_password)
submit_button.pack(pady=10)

root.mainloop()