from tkinter import *
from tkinter import ttk
 
window = Tk()
window.title("My first GUI program")
window.minsize(width= 500, height=300)
 
 
# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()
 
my_label["text"] = "New Text"
my_label.config(text="New Text")
 
## UPDATES UI TEXT STATE
def button_clicked():
    my_label.config(text="I got clicked")
 
 
## TRIGGERS FUNCTION ON CLICK
button = ttk.Button(text="Click Me", command=button_clicked).pack()
 
# Entry
input = Entry(width = 10)
input.pack()
 
 
 
window.mainloop()

