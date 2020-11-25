from tkinter import *

def function():
    print(myInput.get())
    entry_text = myInput.get()

root = Tk()

entry_text = StringVar()
myInput = Entry(root,
                textvariable= "Click ME",
                width=100,
                bg='white',
                fg='black',
                borderwidth=5)


myButton = Button(root,
                  text= "Click ME",
                  command=function,
                  padx=10,
                  pady=10,
                  bg='grey',
                  fg='blue')

myLabel = Label(root, text=entry_text)

myInput.pack()
myButton.pack()
myLabel.pack()

root.mainloop()
