import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Your Password Manager")
root.geometry("500x400")

# Label
label = ttk.Label(root, text="Type in your master password:")
label.pack(pady=10)

root.mainloop()