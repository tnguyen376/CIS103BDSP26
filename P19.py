#Tyler Nguyen
import tkinter as tk

# create window
root = tk.Tk()
root.title("Face")

# create canvas
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

# head (big circle)
canvas.create_oval(50, 30, 250, 230, outline="purple", width=3)

# left eye (red)
canvas.create_oval(90, 70, 130, 110, fill="teal")

# right eye (blue)
canvas.create_oval(170, 80, 210, 110, fill="green")

# mouth (yellow rectangle)
canvas.create_rectangle(110, 140, 190, 155, fill="pink")

# triangle (chin / beard)
canvas.create_polygon(120, 200, 180, 200, 150, 250, fill="red", outline="orange", width=13)

# run window
root.mainloop()
