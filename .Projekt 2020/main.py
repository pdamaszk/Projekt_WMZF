import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from numpy import sin,cos
import numpy as np

y = True
def double_pen_ani_wyk(L1, th1, M1, L2, th2, M2):
    from numpy import sin, cos

    import matplotlib.pyplot as plt
    import scipy.integrate as integrate
    import matplotlib.animation as animation

    G = 9.8         # [m/s^2]       przyspieszenie ziemskie

    # L1 = 0.3        # [m]           dlugosc pierwszego wahadla
    # th1 = 90.0      # [stopnie]     kąt nachylenia pierwszego wahadla
    # M1 = 100.0      # [kg]          masa pierwszego wahadla
    #
    # L2 = 1.0        # [m]           dlugosc drugiego wahadla
    # th2 = -90.0     # [stopnie]     kąt nachylenia drugiego wahadla
    # M2 = 2.0        # [kg]          masa drugiego wahadla

    w1 = 0.0        # [m/s]         prędkość poczatkowa pierwszego wahadla
    w2 = 0.0        # [m/s]         prędkość poczatkowa drugiego wahadla

    dt = 0.05       # [s]           delta - dokładność obliczeń
    t = np.arange(0, 60, dt)



    def pochodna(state, t):

        dydx = np.zeros_like(state)
        dydx[0] = state[1]

        delta = state[2] - state[0]
        den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
        dydx[1] = ((M2 * L1 * state[1] * state[1] * sin(delta) * cos(delta)
                    + M2 * G * sin(state[2]) * cos(delta)
                    + M2 * L2 * state[3] * state[3] * sin(delta)
                    - (M1+M2) * G * sin(state[0]))
                   / den1)

        dydx[2] = state[3]

        den2 = (L2/L1) * den1
        dydx[3] = ((- M2 * L2 * state[3] * state[3] * sin(delta) * cos(delta)
                    + (M1+M2) * G * sin(state[0]) * cos(delta)
                    - (M1+M2) * L1 * state[1] * state[1] * sin(delta)
                    - (M1+M2) * G * sin(state[2]))
                   / den2)

        return dydx



    # initial state
    state = np.radians([th1, w1, th2, w2])

    # integrate your ODE using scipy.integrate.
    global y
    y = integrate.odeint(pochodna, state, t)

    x1 = L1*sin(y[:, 0])
    y1 = -L1*cos(y[:, 0])

    x2 = L2*sin(y[:, 2]) + x1
    y2 = -L2*cos(y[:, 2]) + y1

    fig = plt.figure()
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-1.1*(L1+L2), 1.1*(L1+L2)), ylim=(-1.1*(L1+L2), L1+0.5*L2))
    # ax.set_ylim([-1.1*(L1+L2), 1.1*L1])
    # ax.set_xlim([-1.1*(L1 + L2), 1.1*(L1+L2)])
    # print(np.size(y))
    ax.set_aspect('equal')
    ax.grid()

    line, = ax.plot([], [], 'o-', lw=2)
    time_template = 'time = %.2fs'
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


    def init():
        line.set_data([], [])
        time_text.set_text('')
        return line, time_text


    def animate(i):
        thisx = [0, x1[i], x2[i]]
        thisy = [0, y1[i], y2[i]]

        line.set_data(thisx, thisy)
        time_text.set_text(time_template % (i*dt))
        return line, time_text


    ani = animation.FuncAnimation(fig, animate, range(1, len(y)),
                                  interval=dt*1000, blit=True, init_func=init)
    plt.show()

def rysuj():
    while True:
        checkvariables()
        if wyjsc == True:
            double_pen_ani_wyk(float(Entry_L1.get()), float(Entry_Th1.get()), float(Entry_M1.get()),
                               float(Entry_L2.get()), float(Entry_Th2.get()), float(Entry_M2.get()))
            break

# definicja icony okna
def pull_icon(root,icon):
    root.iconbitmap(icon)
# definicja srodek szerokosci okna canvas
def canvas_X(x):
    return canvas_width // 2 + x
# definicja srodek wysokosci okna canvas
def canvas_Y(y):
    return canvas_height // 2 - y
# definicja przetwarzania okna DODATKI
def Calc_please(L1, Th1, L2, Th2):
    x1 = (L1 * sin(Th1))
    y1 = (-L1 * cos(Th1))
    x2 = (x1 + L2 * sin(Th2))
    y2 = (y1 - L2 * cos(Th2))

    x1y1 = f"({round(x1, 2)}, {round(y1, 2)})"
    x2y2 = f"({round(x2, 2)}, {round(y2, 2)})"
    W1.set(x1y1)
    W2.set(x2y2)
    draw_pendulum(x1, y1, x2, y2)
# definicja rysowania wahadła <wizualizacja>
def draw_pendulum(x1, y1, x2, y2):
    norm_x = (abs(x1) + abs(x2))/canvas_X(0)
    norm_y = (abs(y1) + abs(y2))/canvas_Y(0)
    if norm_x > norm_y:
        norm = norm_x
    else:
        norm = norm_y
    if norm > 1:
        norm *= 1.1
    else:
        norm *= 1.1

    x0 = canvas_X(0)
    y0 = canvas_Y(0)
    x1 /= norm
    x1 = canvas_X(int(x1))
    y1 /= norm
    y1 = canvas_Y(int(y1))
    x2 /= norm
    x2 = canvas_X(int(x2))
    y2 /= norm
    y2 = canvas_Y(int(y2))
    C.delete("all")
    coord_ox = 20, y0, canvas_width-20, y0
    coord_oy = x0, 20, x0, canvas_height-20
    coord1 = x0, y0, x1, y1
    coord2 = x1, y1 , x2, y2
    C.create_line(coord_ox, fill='#cccccc')
    C.create_line(coord_oy, fill='#cccccc')
    C.create_line(coord1, fill='black', width=2)
    C.create_line(coord2, fill='black', width=2)
    create_circle(C,x0, y0, 3, fill="black", outline="black", width=1)
    create_circle(C,x1, y1, 5, fill="blue", outline="black", width=2)
    create_circle(C,x2, y2, 5, fill="red", outline="black", width=2)

# rysowanie okręgu w oknie <canvas>
def create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)

# definicja reakcji na klawisz enter
def eventEnter(event):
    # print(event.keysym)
    if event.keysym == "Return":
        checkvariables()
    # try:
    #     int(event.keysym)
    #     checkvariables()
    # except:
    #     pass

# definicja sprawdzenie danych w oknie wahadel
def checkvariables():
    try:
        L1 = float(Entry_L1.get())
        print(float(Entry_L1.get()))
    except:
        # Entry_L1.delete(0, tk.END)
        messagebox.showwarning(title="Ostzreżenie", message="\tNiepoprawna długość ramienia górnego wahadła\t")
        Entry_L1.focus()
        return False

    try:
        Th1 = float(Entry_Th1.get())

    except:
        # Entry_Th1.delete(0, tk.END)
        messagebox.showwarning(title="Ostzreżenie", message="\tNiepoprawny kąt górnego wahadła\t")
        Entry_Th1.focus()
        return False

    try:
        L2 = float(Entry_L2.get())
    except:
        # Entry_L2.delete(0, tk.END)
        messagebox.showwarning(title="Ostzreżenie", message="\tNiepoprawae długość ramienia dolnego wahadła\t")
        Entry_L2.focus()
        return False
    try:
        Th2 = float(Entry_Th2.get())
        Calc_please(L1, Th1, L2, Th2)
    except:
        # Entry_Th2.delete(0, tk.END)
        messagebox.showwarning(title="Ostzreżenie", message="\tNiepoprawny kąt dolnego wahadła\t")
        Entry_Th2.focus()
        return False
    if keypressed:
        try:
            M1 = float(Entry_M1.get())
        except:
            Entry_M1.delete(0, tk.END)
            messagebox.showwarning(title="Ostzreżenie", message="\tNiepoprawna wartość masy górnego wahadła\t")
            Entry_M1.focus()
            return False
        try:
            M2 = float(Entry_M2.get())
        except:
            Entry_M2.delete(0, tk.END)
            messagebox.showwarning(title="Ostzreżenie", message="\tNiepoprawna wartość masy dolnego wahadła\t")
            Entry_M2.focus()
            return False
        return True


# definicja trybu testowego - testowanie zawartosci okna
def test_interfecu():
    global test_id
    test_id = 1
# configuracja - parametry trybu testowego
test_colours = { 'title':(None,'yellow'),
              'left_frame':(None,'green'),
              'right_frame':(None,'orange'),
              'canvas':(None,'blue'),
              'botton':(None,'blue'),
              'adds':(None,'pink') }


test_id = 0
test=False
keypressed = False

# icona
window_ico = 'ico2_32_32_2.ico'
# tytuł okna
window_title = " Wahadło podwójne - v1.0 Beta"
# Czcionki
global_font = "Calibri"
main_font = f"{global_font} 12 "
sub_font = f"{global_font} 10 italic"
title_font = f"{global_font} 20 bold italic"
# pełny ekran < wysokosc / szerokosc >
window_width_change = False
window_height_change = False

padx_label = 8
align_entry = 'right'
#
color_list = (None, 'white', 'red')
bg_canvas = color_list[1]
bg_button = color_list[0]
window_width = 600
window_height = 550
canvas_width = 300
canvas_height = 300

if test:
    test_interfecu()

Window_wahadlo = tk.Tk()
x_position = Window_wahadlo.winfo_screenwidth()
y_position = Window_wahadlo.winfo_screenheight()

window_Xposition = (x_position-window_width)//2
window_Yposition = (y_position-window_height)//2
Window_wahadlo.update_idletasks()
Window_wahadlo.option_add( "*font", main_font)
# Window_wahadlo.option_add('*Dialog.msg.font', main_font)

## Okno główne
Window_wahadlo.title(window_title)
Window_wahadlo.geometry(f"{window_width}x{window_height}+{window_Xposition}+{window_Yposition}")
Window_wahadlo.resizable(width=window_width_change, height=window_height_change)
pull_icon(Window_wahadlo, window_ico)

# ------------------------------Tytuł ----------------------
Window_Frame = tk.Frame(Window_wahadlo, padx=5, pady=5,
                        bg=test_colours['title'][test_id])
Window_Frame.grid(row=0, column=0, columnspan=2)
Window_Label = tk.Label(Window_Frame, text=window_title, font=title_font)
Window_Label.pack(fill="both", expand="yes")

# -------------------------okno canvas----------------------
Frame_visualisation = tk.Label(Window_wahadlo, padx=5, pady=5,
                               bg=test_colours['right_frame'][test_id])
Frame_visualisation.grid(row=1, column=1, sticky='wn')
Labelframe_visualisation = tk.LabelFrame(Frame_visualisation,
                                         padx=5, pady=5,
                                         text="Podgląd warunku poczaątkowego",
                                         font=sub_font)
Labelframe_visualisation.grid(row=0, column=0, sticky='w')

C = tk.Canvas(Labelframe_visualisation, height=canvas_height, width=canvas_width, bg=bg_canvas)
C.pack()

## Frame LEWY
frame_left = tk.Frame(Window_wahadlo, padx=5, pady=5, bg=test_colours['left_frame'][test_id])
frame_left.grid(row=1, column=0, sticky='wn')

##  (frame lewy)
## ----- # górny frame "Górne wahadlo"
Left_Frame = tk.LabelFrame(frame_left, padx=5, pady=5, text="Górne wahadlo", font=sub_font)
Left_Frame.grid(row=0, column=0)

label_L1 = tk.Label(Left_Frame, text=f"Długość wahadła L\u2081", padx=padx_label)
label_Th1 = tk.Label(Left_Frame, text=f"Kąt {chr(952)}\u2081", padx=padx_label)
label_M1 = tk.Label(Left_Frame, text="Masa M\u2081", padx=padx_label)

Entry_L1 = tk.Entry(Left_Frame, borderwidth=2, width=10)
Entry_Th1 = tk.Entry(Left_Frame, borderwidth=2, width=10)
Entry_M1 = tk.Entry(Left_Frame, borderwidth=2, width=10)

label_L1.grid(row=0, column=0, sticky='e')
label_Th1.grid(row=1, column=0, sticky='e')
label_M1.grid(row=2, column=0, sticky='e')
Entry_L1.grid(row=0, column=1)
Entry_Th1.grid(row=1, column=1)
Entry_M1.grid(row=2, column=1)

## ----- # dolny frame 1 "Dolne wahadlo"
Left_Frame_2 = tk.LabelFrame(frame_left, padx=5, pady=5, text="Dolne wahadlo", font=sub_font)
Left_Frame_2.grid(row=1, column=0)

label_L2 = tk.Label(Left_Frame_2, text=f"Długość wahadła L\u2082", padx=padx_label)
label_Th2 = tk.Label(Left_Frame_2, text=f"Kąt {chr(952)}\u2082", padx=padx_label)
label_M2 = tk.Label(Left_Frame_2, text="Masa M\u2082", padx=padx_label)

Entry_L2 = tk.Entry(Left_Frame_2, borderwidth=2, width=10)
Entry_Th2 = tk.Entry(Left_Frame_2, borderwidth=2, width=10)
Entry_M2 = tk.Entry(Left_Frame_2, borderwidth=2, width=10)

label_L2.grid(row=0, column=0, sticky='e')
label_Th2.grid(row=1, column=0, sticky='e')
label_M2.grid(row=2, column=0, sticky='e')
Entry_L2.grid(row=0, column=1)
Entry_Th2.grid(row=1, column=1)
Entry_M2.grid(row=2, column=1)

# ----- # dolny frame 2 "dodatki 1"
Right_Frame = tk.Frame(frame_left, padx=5, pady=5, width=350)
Right_Frame.grid(row=2, column=0)

W1 = tk.StringVar()
W2 = tk.StringVar()

label_W0 = tk.Label(Right_Frame, text=f"(x\u2080, y\u2080) = ", width=15, anchor='e')
label_W1 = tk.Label(Right_Frame, text=f"(x\u2081, y\u2081) = ", width=15, anchor='e')
label_W2 = tk.Label(Right_Frame, text=f"(x\u2082, y\u2082) = ", width=15, anchor='e')

label_W01 = tk.Label(Right_Frame, text="(0, 0)", width=10, anchor='w')
label_W11 = tk.Label(Right_Frame, textvariable=W1, width=10, anchor='w')
label_W21 = tk.Label(Right_Frame, textvariable=W2, width=10, anchor='w')

Button_calc_coord = tk.Button(Right_Frame,
                              text= "Pokaż podgląd",
                              command=checkvariables,
                              padx=10,
                              pady=2,
                              relief='raised',
                              borderwidth=4,
                              bg=bg_button)

label_W0.grid(row=1, column=0, sticky='e')
label_W1.grid(row=2, column=0, sticky='e')
label_W2.grid(row=3, column=0, sticky='e')
label_W01.grid(row=1, column=1, sticky='w')
label_W11.grid(row=2, column=1, sticky='w')
label_W21.grid(row=3, column=1, sticky='w')

Button_calc_coord.grid(row=4, column=0, columnspan=2)

Window_Frame_bottom = tk.Frame(Window_wahadlo, padx=5, pady=5, bg=test_colours['botton'][test_id], width=700, height=200)
Window_Frame_bottom.grid(row=2, column=0, columnspan=2, sticky='w')
# Okno Notebook
Bottom_Frame = tk.LabelFrame(Window_Frame_bottom, padx=5, pady=5, text="", font=sub_font)
Bottom_Frame.grid(row=0, column=0)

# Notebook
nb = ttk.Notebook(Bottom_Frame)
nb.grid(row=0, column=0, columnspan=2, sticky='NEWS')

# Tworzenie pierwszej zakładki
f1 = tk.Frame(nb)
f1_menu = tk.Label(f1, text="tu beda do wyboru wykresy")
f1_menu.grid(row=0, column=0)
f1_button = tk.Button(f1, text= "Wykres",
                              command=rysuj,
                              padx=10,
                              pady=2,
                              relief='raised',
                              borderwidth=4,
                              bg=bg_button)
f1_button.grid(row=1, column=0)

# Dodawanie pierwszej zakładki
nb.add(f1, text="Wykresy")
# Tworzenie drugiej zakładki
f2 = tk.Frame(nb)
# Dodawanie drugiej zakładki
nb.add(f2, text="Ustawienia")
# Tworzenie trzeciej zakładki
f3 = tk.Frame(nb)
f1_menu3 = tk.Label(f3, text="zrób ikonke do naszego \nprogramu !!", font=title_font, bg='white', width=25, height=3)
f1_menu3.grid(row=0, column=0)

# Dodawanie trzeciej zakładki
nb.add(f3, text="Jan Kurek")

nb.select(f1)

nb.enable_traversal()

# button_2 = tk.Button(sq_frame2)
# button_2.grid(row=0, column=0, sticky='n')


# kursor na pole Entry_L1
Entry_L1.focus()
# zbieranie danych o wcisnietym klawiszu
Window_wahadlo.bind("<Key>", eventEnter)

Window_wahadlo.mainloop()
