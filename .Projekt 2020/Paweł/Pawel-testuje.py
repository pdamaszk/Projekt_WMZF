import tkinter as tk
from tkinter.colorchooser import askcolor
color="#6A9662"

def callback():
    result = askcolor(color=color,
                      title="Bernd's Colour Chooser")
    print(result)
    b1.configure(bg=result[1])



root = tk.Tk()
b1 = tk.Button(root,
               text='Choose Color',
               fg="darkgreen",
               bg="red",
               command=callback)
b1.grid(column=0, row=0)
b2 = tk.Button(text='Quit',
          command=root.quit,
          fg="red")
b1.grid(column=1, row=0)

tk.mainloop()