def tkinter009():
    import tkinter as tk


    master = tk.Tk()
    tk.Label(master, text="").grid(row=0)
    tk.Label(master, text="Last Name").grid(row=1)
    tk.Label(master, text="First Name").grid(row=2)
    tk.Label(master, text="Last Name").grid(row=3)
    tk.Label(master, text="First Name").grid(row=4)
    tk.Label(master, text="Last Name").grid(row=5)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)
    e4 = tk.Entry(master)
    e5 = tk.Entry(master)
    e6 = tk.Entry(master)
    # e1.insert(10, "Miller")
    # e2.insert(10, "Jill")

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)
    e6.grid(row=5, column=1)

    tk.Button(master,
              text='Quit',
              command=master.quit).grid(row=10,
                                        column=0,
                                        sticky=tk.W,
                                        pady=4)
    tk.Button(master, text='Show').grid(row=10,
                                                                   column=1,
                                                                   sticky=tk.E,
                                                                   pady=4)

    master.mainloop()

    tk.mainloop()

tkinter009()