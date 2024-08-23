import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer.")

        # Define character sets
        chars = string.ascii_letters
        if include_numbers.get():
            chars += string.digits
        if include_symbols.get():
            chars += string.punctuation

        if not chars:
            raise ValueError("At least one character type must be selected.")
        
        # Generate the password
        password = ''.join(random.choice(chars) for _ in range(length))
        result_label.config(text=f"Generated Password: {password}")

    except ValueError as ve:
        messagebox.showwarning("Warning", str(ve))

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create widgets
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(root, width=10)
length_entry.grid(row=0, column=1, padx=10, pady=10)

include_numbers = tk.BooleanVar()
numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=include_numbers)
numbers_check.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

include_symbols = tk.BooleanVar()
symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=include_symbols)
symbols_check.grid(row=2, column=0, padx=10, pady=5, columnspan=2)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="Generated Password:")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
