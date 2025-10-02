from tkinter import *

# Setting up Main Window
root = Tk()
root.geometry("400x300")
root.title("Main Window")

# Function to open New (Top Level) Window
def topwin():
    # Setting up Top Window
    top = Toplevel()
    top.geometry("180x100")
    top.title("Toplevel Window")

    # Adding a label widget to Top Window
    lbl_top = Label(top, text="This is toplevel window")
    lbl_top.pack()

# Adding a label and button Widget to Root (Main) Window
lbl_root = Label(root, text="This is root window")
btn = Button(root, text="Click here to open another window", command=topwin)

# Arranging widgets
lbl_root.pack()
btn.pack()

root.mainloop()
