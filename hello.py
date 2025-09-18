import tkinter as tk
from tkinter import messagebox
def calculate_product():
    """Calculates the product of two numbers and displays the result."""
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")
window = tk.Tk()
window.title("Product Calculator")
label1 = tk.Label(window, text="Enter first number:")
label1.grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1, padx=5, pady=5)
label2 = tk.Label(window, text="Enter second number:")
label2.grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=5, pady=5)
calculate_button = tk.Button(window, text="Calculate", command=calculate_product)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)
result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2)
window.mainloop()
