import tkinter as tk
cash = 0
window = tk.Tk()
window.geometry(newGeometry="450x350")
window.configure(bg = "#808080")
def addcash():
    global cash
    cash = cash + 1
    lblcash.configure(text = cash)
def on_press(e):
    button.configure(highlightbackground="gold")
def on_release(e):
    button.configure(highlightbackground="#808080")
lbl = tk.Label(text = "Welcome to Clicker", background="#808080")
button = tk.Button(text="Click Me!", highlightbackground="#808080", command=lambda:addcash())
button.bind("<ButtonPress>", on_press)
button.bind("<ButtonRelease>", on_release)
lblcash = tk.Label(text=cash, background="#808080")
lbl.pack()
button.pack()
lblcash.pack()
window.mainloop()

