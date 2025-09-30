from tkinter import *
from tkinter import messagebox

# Function to calculate interest
def calculate_interest():
    try:
        # Get user inputs
        principal = float(entry_principal.get())
        time = float(entry_time.get())
        rate = float(entry_rate.get())

        # Simple Interest
        si = (principal * time * rate) / 100

        # Compound Interest
        ci = principal * ((1 + rate/100) ** time - 1)

        # Display result
        result_si.config(text=f"Simple Interest: {si:.2f}")
        result_ci.config(text=f"Compound Interest: {ci:.2f}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

# Tkinter window setup
window = Tk()
window.title("Simple & Compound Interest Calculator")
window.geometry("400x300")
window.resizable(False, False)

# Labels and Entry fields
Label(window, text="Principal Amount:", font=("Arial", 12)).pack(pady=5)
entry_principal = Entry(window, font=("Arial", 12))
entry_principal.pack(pady=5)

Label(window, text="Time (years):", font=("Arial", 12)).pack(pady=5)
entry_time = Entry(window, font=("Arial", 12))
entry_time.pack(pady=5)

Label(window, text="Rate of Interest (%):", font=("Arial", 12)).pack(pady=5)
entry_rate = Entry(window, font=("Arial", 12))
entry_rate.pack(pady=5)

# Calculate Button
Button(window, text="Calculate", font=("Arial", 12, "bold"), command=calculate_interest).pack(pady=10)

# Results
result_si = Label(window, text="Simple Interest: ", font=("Arial", 12), fg="blue")
result_si.pack(pady=5)

result_ci = Label(window, text="Compound Interest: ", font=("Arial", 12), fg="green")
result_ci.pack(pady=5)

# Run the application
window.mainloop()
