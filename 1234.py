import tkinter as tk
from tkinter import messagebox
from datetime import date, datetime

def calculate_age():
    """Calculates age based on user input and displays it."""
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        birthdate = date(year, month, day)
        today = date.today()

        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

        result_label.config(text=f"Your age is: {age} years")

    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use integers for day, month, and year.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Create main window
window = tk.Tk()
window.title("Age Calculator")

# Labels and entry fields for date of birth
day_label = tk.Label(window, text="Day:")
day_label.grid(row=0, column=0, padx=5, pady=5)
day_entry = tk.Entry(window)
day_entry.grid(row=0, column=1, padx=5, pady=5)

month_label = tk.Label(window, text="Month:")
month_label.grid(row=1, column=0, padx=5, pady=5)
month_entry = tk.Entry(window)
month_entry.grid(row=1, column=1, padx=5, pady=5)

year_label = tk.Label(window, text="Year:")
year_label.grid(row=2, column=0, padx=5, pady=5)
year_entry = tk.Entry(window)
year_entry.grid(row=2, column=1, padx=5, pady=5)

# Button to calculate age
calculate_button = tk.Button(window, text="Calculate Age", command=calculate_age)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label to display the result
result_label = tk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2)

window.mainloop()
