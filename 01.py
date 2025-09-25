import tkinter as tk

def convert_inches_to_cm():
    """Converts inches to centimeters and displays the result."""
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{inches} inches is equal to {cm:.2f} centimeters")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a number.")

# Create main window
window = tk.Tk()
window.title("Inches to Centimeters Converter")

# Create and place widgets
label = tk.Label(window, text="Enter length in inches:")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=5)

convert_button = tk.Button(window, text="Convert", command=convert_inches_to_cm)
convert_button.pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()
