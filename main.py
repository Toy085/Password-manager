import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("My Application")
root.geometry("400x300")

# Label
label = ttk.Label(root, text="Hello, World!")
label.pack(pady=10)

# Button
def on_click():
    label.config(text="Button clicked!")

button = ttk.Button(root, text="Click Me", command=on_click)
button.pack(pady=10)

# Entry
entry = ttk.Entry(root, width=30)
entry.pack(pady=10)

root.mainloop()