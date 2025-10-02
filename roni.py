import tkinter as tk
from tkinter import messagebox

def check_password_strength():
    password = password_entry.get()
    length = len(password)

    if length == 0:
        strength_label.config(text="Strength: Empty", fg="gray")
    elif length < 6:
        strength_label.config(text="Strength: Weak", fg="red")
    elif 6 <= length < 10:
        strength_label.config(text="Strength: Medium", fg="orange")
    else:
        strength_label.config(text="Strength: Strong", fg="green")

# Create the main application window
app = tk.Tk()
app.title("Password Strength Checker")
app.geometry("300x150") # Set initial window size

# Create a label for instructions
instruction_label = tk.Label(app, text="Enter your password:")
instruction_label.pack(pady=10)

# Create an Entry widget for password input
password_entry = tk.Entry(app, show="*", width=30) # show="*" hides the password
password_entry.pack(pady=5)
password_entry.bind("<KeyRelease>", lambda event: check_password_strength()) # Check on every key release

# Create a button to check strength (although it also checks on key release)
check_button = tk.Button(app, text="Check Strength", command=check_password_strength)
check_button.pack(pady=5)

# Create a label to display the password strength
strength_label = tk.Label(app, text="Strength: ", font=("Arial", 12, "bold"))
strength_label.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()
