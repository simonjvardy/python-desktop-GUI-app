from tkinter import *

# Initiate a new window
window=Tk()

# The GUI Window buttons and functions goes here

def km_to_miles():
    print(e1_value.get())
    t1.insert(END)  # Append the text to the bottom of the text field

# Define a new button
b1=Button(window, text="Execute", command=km_to_miles)

# Add the button to the window
# b1.pack()
b1.grid(row=0, column=0)

# User input field
e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

# Text display field
t1=Text(window, height=1, width=20)
t1.grid(row=0,column=2)

# This should always be at the end of the code
window.mainloop()