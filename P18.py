#Tyler Nguyen
from tkinter import *

def calculate():
    try:
        k = float(kelvin_entry.get())

        if k <= 0:
            error("Kelvin must be greater than 0")
            return

        c = k - 273.15
        f = (9/5) * (k - 273) + 32

        celsius_entry.delete(0, END)
        fahrenheit_entry.delete(0, END)

        celsius_entry.insert(0, str(round(c, 2)))
        fahrenheit_entry.insert(0, str(round(f, 2)))

        root.config(bg="lightgreen")

    except:
        error("Invalid input (must be a number)")

def error(message):
    error_entry.delete(0, END)
    error_entry.insert(0, message)
    root.config(bg="lightcoral")

def clear():
    kelvin_entry.delete(0, END)
    celsius_entry.delete(0, END)
    fahrenheit_entry.delete(0, END)
    error_entry.delete(0, END)
    root.config(bg="lightblue")  # reset to default color

# Window
root = Tk()
root.title("Temperature Conversion")
root.geometry("350x250")
root.config(bg="lightblue")  # <-- default background color

# Labels (match background)
Label(root, text="Kelvin", bg="lightblue").grid(row=0, column=0)
Label(root, text="Celsius", bg="lightblue").grid(row=1, column=0)
Label(root, text="Fahrenheit", bg="lightblue").grid(row=2, column=0)

# Entries
kelvin_entry = Entry(root)
celsius_entry = Entry(root)
fahrenheit_entry = Entry(root)
error_entry = Entry(root, width=30)

kelvin_entry.grid(row=0, column=1)
celsius_entry.grid(row=1, column=1)
fahrenheit_entry.grid(row=2, column=1)
error_entry.grid(row=3, column=0, columnspan=2, pady=10)

# Buttons
Button(root, text="CALC", command=calculate).grid(row=4, column=0)
Button(root, text="CLEAR", command=clear).grid(row=4, column=1)

root.mainloop()
