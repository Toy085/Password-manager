import time
import tkinter as tk
from tkinter import ttk, messagebox
import os
import hashlib
import base64
from cryptography.fernet import Fernet
import json

# Logic Functions
def master_password_exists() -> bool:
    return os.path.exists("master.key")

def hash_master_password(password: str) -> bytes:
    salt = os.urandom(16)
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt,
        200_000
    )
    return salt + key

def get_encryption_key(master_password: str) -> bytes:
    hasher = hashlib.sha256()
    hasher.update(master_password.encode())
    return base64.urlsafe_b64encode(hasher.digest())

def save_master_password(password: str):
    hashed = hash_master_password(password)
    with open("master.key", "wb") as f:
        f.write(hashed)

def check_master_password(password: str) -> bool:
    with open("master.key", "rb") as f:
        data = f.read()

    salt = data[:16]
    stored_key = data[16:]

    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt,
        200_000
    )

    return new_key == stored_key

def submit_password():
    master_password = password_entry.get()

    if not master_password:
        messagebox.showerror("Error", "Password cannot be empty")
        return

    if master_password_exists():
        if check_master_password(master_password):
            open_main_window(master_password)
            root.withdraw()
        else:
            messagebox.showerror("Error", "Incorrect password")
            time.sleep(1)
    else:
        save_master_password(master_password)
        messagebox.showinfo("Success", "Master password created!")
        open_main_window(master_password)
        root.withdraw()

# Application window for master password input
root = tk.Tk()
root.title("Your Password Manager")
root.geometry("300x200")

label = ttk.Label(root, text="Type in your master password:")

if master_password_exists():
    label.config(text="Type in your master password:")
else:
    label.config(text="Create a master password:")

label.pack(pady=10)

password_entry = ttk.Entry(root, show="*")
password_entry.pack(pady=10)


submit_button = ttk.Button(root, text="Submit", command=submit_password)
submit_button.pack(pady=10)

def set_app_icon(window):
    icon = tk.PhotoImage(file="icon.png")
    window.iconphoto(True, icon)

set_app_icon(root)

# The main application window
def open_main_window(master_pwd):
    main_window = tk.Toplevel(root)
    main_window.title("Password Vault")
    main_window.geometry("500x400")

    encryption_key = get_encryption_key(master_pwd)
    cipher = Fernet(encryption_key)
    VAULT_FILE = "vault.dat"

    def load_vault():
        if not os.path.exists(VAULT_FILE):
            return {}
        try:
            with open(VAULT_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            messagebox.showerror("Error", "Unknown error loading vault.")
            return {}

    def save_to_vault(data):
        with open(VAULT_FILE, "w") as f:
            json.dump(data, f, indent=4)

    vault_data = load_vault()

    top_frame = ttk.Frame(main_window)
    top_frame.pack(pady=10)

    middle_frame = ttk.Frame(main_window)
    middle_frame.pack(pady=10)

    bottom_frame = ttk.Frame(main_window)
    bottom_frame.pack(pady=10)

    ttk.Label(top_frame, text="Your Passwords:", font=("Arial", 14)).pack()

    list_scroll = ttk.Scrollbar(middle_frame)
    list_scroll.pack(side="right", fill="y")
    
    account_list = tk.Listbox(middle_frame, yscrollcommand=list_scroll.set, height=10)
    account_list.pack(fill="both", expand=True)
    list_scroll.config(command=account_list.yview)

    def update_list():
        account_list.delete(0, tk.END)
        for website in vault_data:
            account_list.insert(tk.END, website)

    update_list()

    bottom_frame = ttk.Frame(main_window)
    bottom_frame.pack(pady=10, padx=10, fill="x")

    # Input Fields Grid
    input_frame = ttk.Frame(bottom_frame)
    input_frame.pack(pady=5)

    ttk.Label(input_frame, text="Website/App:").grid(row=0, column=0, padx=5, sticky="e")
    site_entry = ttk.Entry(input_frame, width=30)
    site_entry.grid(row=0, column=1, padx=5, pady=2)

    ttk.Label(input_frame, text="Username/Email:").grid(row=1, column=0, padx=5, sticky="e")
    user_entry = ttk.Entry(input_frame, width=30)
    user_entry.grid(row=1, column=1, padx=5, pady=2)

    ttk.Label(input_frame, text="Password:").grid(row=2, column=0, padx=5, sticky="e")
    pass_entry = ttk.Entry(input_frame, width=30, show="*") # Hide input
    pass_entry.grid(row=2, column=1, padx=5, pady=2)

root.mainloop()