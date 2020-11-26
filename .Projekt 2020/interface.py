import tkinter as tk
from tkinter import messagebox
from numpy import sin,cos
#
def Calc_please(L1, Th1, L2, Th2):
    x1 = round(L1 * sin(Th1), 2)
    y1 = round(- L1 * cos(Th1))
    x2 = round(x1 + L2 * sin(Th2))
    y2 = round(y1 - L2 * cos(Th1))
    x1y1 = f"({x1}, {y1})"
    x2y2 = f"({x2}, {y2})"
    W1.set(x1y1)
    W2.set(x2y2)
    return 0

def checkvariables():
    try:
        L1 = float(Entry_L1.get())
        Th1 = float(Entry_Th1.get())
        M1 = float(Entry_M1.get())
        L2 = float(Entry_L2.get())
        Th2 = float(Entry_Th2.get())
        M2 = float(Entry_M2.get())
        Calc_please(L1, Th1, L2, Th2)

    except:
        messagebox.showwarning(title="Ostzreżenie", message="\tNiepoprawde dane\t")


# testowanie zawartosci okna
def test_interfecu():
    global test_id
    test_id = 1
# configuracja testowania framów interfacu
test_colours = { 'title':(None,'yellow'),
              'left_frame':(None,'green'),
              'right_frame':(None,'orange'),
              'canvas':(None,'blue'),
              'botton':(None,'blue'),
              'adds':(None,'pink') }


test_id = 0
test=True


window_title = " Wahadło podwójne - v1.0"

main_font = "Times 12 "
sub_font = "Times 10 italic"
title_font = "Times 20 bold italic"

window_width = 650
window_height = 480
window_Xposition = 100
window_Yposition = 100
window_width_change = True
window_height_change = True

padx_label = 8

canvas_width = 280
canvas_height = 300

if test:
    test_interfecu()

Window_wahadlo = tk.Tk()
Window_wahadlo.update_idletasks()
Window_wahadlo.option_add( "*font", main_font)

x_position = Window_wahadlo.winfo_screenwidth()
y_position = Window_wahadlo.winfo_screenheight()

## Okno główne
Window_wahadlo.title(window_title)
Window_wahadlo.geometry(f"{window_width}x{window_height}+{window_Xposition}+{window_Yposition}")
Window_wahadlo.resizable(width=window_width_change, height=window_height_change)
# Window_wahadlo.iconbitmap('c:\sddas')


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

C = tk.Canvas(Labelframe_visualisation, height=canvas_height, width=canvas_width)
C.pack()
coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=30, extent=90, fill="red")

## Frame LEWY
frame_left = tk.Frame(Window_wahadlo, padx=5, pady=5, bg=test_colours['left_frame'][test_id])
frame_left.grid(row=1, column=0, sticky='wn')

##  (frama lewego)
## ----- # górny frame "Górne wahadlo"
Left_Frame = tk.LabelFrame(frame_left, padx=5, pady=5, text="Górne wahadlo", font=sub_font)
Left_Frame.grid(row=0, column=0, sticky='w')



label_L1 = tk.Label(Left_Frame, text=f"Długość wahadła L\u2081", padx=padx_label, width=15)
label_Th1 = tk.Label(Left_Frame, text=f"Kąt {chr(952)}\u2081", padx=padx_label, width=15)
label_M1 = tk.Label(Left_Frame, text="Masa M\u2081", padx=padx_label, width=15)

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
Left_Frame_2.grid(row=1, column=0, sticky='w')
label_L2 = tk.Label(Left_Frame_2, text=f"Długość wahadła L\u2082", padx=padx_label, width=15)
label_Th2 = tk.Label(Left_Frame_2, text=f"Kąt {chr(952)}\u2082", padx=padx_label, width=15)
label_M2 = tk.Label(Left_Frame_2, text="Masa M\u2082", padx=padx_label, width=15)

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
                              text= "Przelicz współrzędne",
                              command=checkvariables,
                              padx=10,
                              pady=2)

# Entry_L2 = tk.Entry(Right_Frame, borderwidth=2, width=10)
# Entry_Th2 = tk.Entry(Right_Frame, borderwidth=2, width=10)
# Entry_M2 = tk.Entry(Right_Frame, borderwidth=2, width=10)

label_W0.grid(row=1, column=0, sticky='e')
label_W1.grid(row=2, column=0, sticky='e')
label_W2.grid(row=3, column=0, sticky='e')
label_W01.grid(row=1, column=1, sticky='w')
label_W11.grid(row=2, column=1, sticky='w')
label_W21.grid(row=3, column=1, sticky='w')
Button_calc_coord.grid(row=4, column=0, columnspan=2)

# Entry_L2.grid(row=0, column=1)
# Entry_Th2.grid(row=1, column=1)
# Entry_M2.grid(row=2, column=1)

Window_Frame_bottom = tk.Frame(Window_wahadlo, padx=5, pady=5, bg=test_colours['botton'][test_id], width=700, height=200)
Window_Frame_bottom.grid(row=2, column=0, columnspan=2)

Bottom_Frame = tk.LabelFrame(Window_Frame_bottom, padx=5, pady=5, text="", font=sub_font)
Bottom_Frame.grid(row=0, column=0)

label_B0 = tk.Label(Bottom_Frame, text=f"(x\u2080, y\u2080) = ", padx=padx_label, width=50, height=3)
label_B0.grid(row=0, column=0, sticky='e')


# button_2 = tk.Button(sq_frame2)
# button_2.grid(row=0, column=0, sticky='n')

Window_wahadlo.mainloop()