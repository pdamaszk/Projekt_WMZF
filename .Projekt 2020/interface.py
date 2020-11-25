import tkinter as tk

window_title = " Wahadło podwójne - v1.0"

main_font = "Times 12 "
sub_font = "Times 10 italic"
title_font = "Times 20 bold italic"

window_width = 600
window_height = 400
window_Xposition = 100
window_Yposition = 100
window_width_change = True
window_height_change = True

padx_label = 8

Window_wahadlo = tk.Tk()
Window_wahadlo.update_idletasks()
Window_wahadlo.option_add( "*font", main_font)


## Okno główne
Window_wahadlo.title(window_title)
Window_wahadlo.geometry(f"{window_width}x{window_height}+{window_Xposition}+{window_Yposition}")
Window_wahadlo.resizable(width=window_width_change, height=window_height_change)

# Window_wahadlo.iconbitmap('c:\sddas')



Window_Frame = tk.Frame(Window_wahadlo, padx=5, pady=5)
# Window_Frame.pack(fill="both", expand="yes")
Window_Frame.grid(row=0, column=0, columnspan=2)
Window_Label = tk.Label(Window_Frame, text=window_title, font=title_font, width=38)
Window_Label.pack(fill="both", expand="yes")

frame_visualisation = tk.Frame(Window_wahadlo, padx=5, pady=5, bg='red')
frame_visualisation.grid(row=1, column=1, sticky='e')

## Frame LEWY
frame_left = tk.Frame(Window_wahadlo, padx=5, pady=5)
frame_left.grid(row=1, column=0, sticky='w')

##  (frama lewego)
## ----- # górny frame "Górne wahadlo"
Left_Frame = tk.LabelFrame(frame_left, padx=5, pady=5, text="Górne wahadlo", font=sub_font)
Left_Frame.grid(row=0, column=0, sticky='w')

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
Right_Frame = tk.LabelFrame(frame_left, padx=5, pady=5, text="Dolne wahadlo", font=sub_font)
Right_Frame.grid(row=1, column=0, sticky='w')
label_L2 = tk.Label(Right_Frame, text=f"Długość wahadła L\u2082", padx=padx_label)
label_Th2 = tk.Label(Right_Frame, text=f"Kąt {chr(952)}\u2082", padx=padx_label)
label_M2 = tk.Label(Right_Frame, text="Masa M\u2082", padx=padx_label)

Entry_L2 = tk.Entry(Right_Frame, borderwidth=2, width=10)
Entry_Th2 = tk.Entry(Right_Frame, borderwidth=2, width=10)
Entry_M2 = tk.Entry(Right_Frame, borderwidth=2, width=10)

label_L2.grid(row=0, column=0, sticky='e')
label_Th2.grid(row=1, column=0, sticky='e')
label_M2.grid(row=2, column=0, sticky='e')
Entry_L2.grid(row=0, column=1)
Entry_Th2.grid(row=1, column=1)
Entry_M2.grid(row=2, column=1)

## ----- # dolny frame 2 "dodatki 1"
# Right_Frame = tk.LabelFrame(frame_left, padx=5, pady=5, text="Współrzeędne", font=sub_font, width=250, height=80)
# Right_Frame.grid(row=2, column=0, sticky='e', padx=5, pady=0, ipadx=0, ipady=0)
# label_W0 = tk.Label(Right_Frame, text=f"(x\u2080, y\u2080) ", padx=padx_label)
# label_W1 = tk.Label(Right_Frame, text=f"(x\u2081, y\u2081) ", padx=padx_label)
# label_W2 = tk.Label(Right_Frame, text=f"(x\u2082, y\u2082) ", padx=padx_label)
#
# Entry_L2 = tk.Entry(Right_Frame, borderwidth=2, width=10)
# Entry_Th2 = tk.Entry(Right_Frame, borderwidth=2, width=10)
# Entry_M2 = tk.Entry(Right_Frame, borderwidth=2, width=10)
#
# label_W0.grid(row=0, column=0, sticky='e')
# label_W1.grid(row=1, column=0, sticky='e')
# label_W2.grid(row=2, column=0, sticky='e')
# Entry_L2.grid(row=0, column=1)
# Entry_Th2.grid(row=1, column=1)
# Entry_M2.grid(row=2, column=1)



# button_2 = tk.Button(sq_frame2)
# button_2.grid(row=0, column=0, sticky='n')

Window_wahadlo.mainloop()