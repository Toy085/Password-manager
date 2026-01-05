import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Your Password Manager")
root.geometry("300x200")

# Label
label = ttk.Label(root, text="Type in your master password:")
label.pack(pady=10)

password_entry = ttk.Entry(root, show="*")
password_entry.pack(pady=10)

def submit_password():
    master_password = password_entry.get()
    if master_password == "1234":
        open_main_window()
        root.withdraw()
    else:
        messagebox.showerror("Error", "Incorrect password")

submit_button = ttk.Button(root, text="Submit", command=submit_password)
submit_button.pack(pady=10)

def open_main_window():
    main_window = tk.Toplevel(root)
    main_window.title("Password Manager")
    main_window.geometry("500x400")

    label = ttk.Label(main_window, text="Welcome to your password vault!")
    label.pack(pady=20)


root.mainloop()