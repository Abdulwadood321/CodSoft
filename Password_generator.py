import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            result_label.config(text="Invalid length. Please enter a positive number.", fg="red")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text="Generated Password: " + password, fg="green")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.", fg="red")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create widgets
length_label = tk.Label(root, text="Enter Password Length:")
length_entry = tk.Entry(root)
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
result_label = tk.Label(root, text="", wraplength=250)

# Place widgets on the grid
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry.grid(row=0, column=1, padx=10, pady=10)
generate_button.grid(row=1, columnspan=2, padx=10, pady=10)
result_label.grid(row=2, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
