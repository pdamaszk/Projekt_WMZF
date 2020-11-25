from tkinter import *

def function():
    print("that is function")

root = Tk()

myInput = Entry(root,
                text= "Click ME",
                width=100,
                bg='white',
                fg='black',
                borderwidth=5)
myInput.pack()

root.mainloop()