from tkinter import *

def function():
    print("that is function")

root = Tk()

myButton = Button(root,
                  text= "Click ME",
                  command=function,
                  padx=10,
                  pady=10,
                  bg='grey',
                  fg='blue')
myButton.pack()

root.mainloop()
