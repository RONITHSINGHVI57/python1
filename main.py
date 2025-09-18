import tkinter as tk
from datetime import date

root = tk.Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

bl = tk.Label(root, text="Hey There!", fg="white", bg="#072F5F", height=1, width=30)

name_lbl = tk.Label(root, text="Full Name", bg="#3895D3")
name_entry = tk.Entry(root)
text_box = tk.Text(root, height=3)

def display():
    name = name_entry.get()
    greet = "Hello " + name + "\n"
    message = "Welcome to the Application! \nToday's date is: " + str(date.today()) + "\n"
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, greet)
    text_box.insert(tk.END, message)

btn = tk.Button(root, text="Begin", command=display, height=1, bg="#1261A0", fg='white')

bl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()
