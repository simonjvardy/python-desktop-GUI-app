from tkinter import *

# Initiate a new window
window=Tk()

# The GUI Window buttons, fields and functions go here:

def km_to_miles():
    miles = float(
        "{:.6f}".format(
            float(
                e1_value.get())*0.621371
            )
        )
    t1.delete('1.0', 'end') # Remove the previous displayed text
    t1.insert("1.0", miles)  # Append the text to the bottom of the text field

# Define the window geometry
window.geometry("300x100")

# Add a window title
window.title("Km to Miles Conversion")

# Define window frame
frame = Frame(window)
frame.grid()

# Label for the input
label_in = Label(frame, text="Kilometers")
label_in.grid(row=0, column=0)

# User input field
e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

# Label for the Results output
label_out = Label(frame, text="Miles")
label_out.grid(row=1, column=0)

# Results Text display field
t1=Text(window, height=1, width=15)
t1.grid(row=1,column=1)

# Define the calculator "convert" button
b1=Button(window, text="Convert", command=km_to_miles)
b1.grid(row=2, column=0)


# This should always be at the end of the code
# and makes sure to keep the main window open
window.mainloop()