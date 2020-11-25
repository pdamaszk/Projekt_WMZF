import tkinter as tk

class FrameName(tk.Frame):
    def __init__(self, the_window, text, width):
        tk.Frame.__init__(self, master=the_window)
        self.variable = tk.StringVar()

        # frame_dane_1 = tk.LabelFrame(the_window, text="dfsfsdf", padx=2, pady=10)
        # frame_dane_1.pack(padx=10, pady=20)

        self.len = tk.Label(self, text="Dlugosc", width=width)
        self.entry_len = tk.Entry(self, textvariable=self.variable, width=10)
        self.theta = tk.Label(self, text="Dlugosc", width=width)
        self.entry_theta = tk.Entry(self, textvariable=self.variable, width=10)
        self.mass = tk.Label(self, text="Dlugosc", width=width)
        self.entry_mass = tk.Entry(self, textvariable=self.variable, width=10)

        self.len.grid(row=0, column=0)
        self.entry_len.grid(row=0, column=1)


class line_label(tk.Frame):
    def __init__(self, the_window, bd, width, height):
        tk.Frame.__init__(self, master=the_window)
        self.line = tk.Label(self, bd=bd, width=width, height=height, text="dfdfd")
        self.line.pack(side=tk.LEFT, padx=5, pady=5)


if __name__ == '__main__':

    ### konfiguracja  ##---------------------------------
    title = "Podwójne wahadło"
    width_window = 600
    height_window = 400
    x_window = 300
    y_window = 300
    width_label = 10


    ### poczatek okna  ##---------------------------------
    Window_wahadlo = tk.Tk()
    Window_wahadlo.title(title)
    Window_wahadlo.geometry(f'{width_window}x{height_window}+{x_window}+{y_window}')


    # frame_dane_1 = tk.LabelFrame(Window_wahadlo, text="dfsfsdf", padx=2, pady=10)
    # frame_dane_1.pack(padx=10, pady=20)


    len_1 = FrameName(Window_wahadlo, 'Dlugosc', width_label)
    theta_1 = FrameName(Window_wahadlo, 'Kat', width_label)
    mass_1 = FrameName(Window_wahadlo, 'Masa', width_label)
    line = line_label(Window_wahadlo, 1, 100, 1)
    len_2 = FrameName(Window_wahadlo, 'Dlugosc', width_label)
    theta_2 = FrameName(Window_wahadlo, 'Kąt', width_label)
    mass_2 = FrameName(Window_wahadlo, 'Masa', width_label)


    len_1.grid(row=0, column=0)
    theta_1.grid(row=1, column=0,)
    mass_1.grid(row=2, column=0)
    line.grid(row=3, column=0)
    len_2.grid(row=4, column=0, sticky=tk.W)
    theta_2.grid(row=5, column=0)
    mass_2.grid(row=6, column=0)



    Window_wahadlo.mainloop()
    ### koniec okna ##---------------------------------
