import tkinter as ttk
# Modify adding a Label                                      # 1
win = ttk.Tk()
aLabel = ttk.Button(win, text="A Label")                      # 2
aLabel.grid(column=0, row=0)                                 # 3


# Button Click Event Callback Function                       # 4
def clickMe():                                               # 5
    action.configure(text="** I have been Clicked! **")
    aLabel.configure(bg='red')

# Adding a Button                                            # 6
action = ttk.Button(win, text="Click Me!", command=clickMe)  # 7
action.grid(column=1, row=0)                                 # 8
ttk.mainloop()