from tkinter import *
from tkinter.ttk import *
from time import strftime

# Create the main window
top = Tk()
top.title("Digital Clock")

# Function to update the time
def none():
    text = strftime('%H:%M:%S %p')  # '%p' for proper AM/PM formatting
    lbl.config(text=text)
    lbl.after(1000, none)

# Label for the clock
lbl = Label(top, font=('digital-7', 50, 'bold'), 
            background='black', foreground='white')
lbl.pack(anchor='center')

# Start the clock
none()

# Run the application
mainloop()
