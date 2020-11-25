import tkinter as tk

window_title = " Wahadło podwójne - v1.0"
window_width = 600
window_height = 400
window_Xposition = 100
window_Yposition = 100
window_width_change = False
window_height_change = False

padx_label = 8

Window_wahadlo = tk.Tk()
Window_wahadlo.update_idletasks()

## Okno główne
Window_wahadlo.title(window_title)
Window_wahadlo.geometry(f"{window_width}x{window_height}+{window_Xposition}+{window_Yposition}")
Window_wahadlo.resizable(width=window_width_change, height=window_height_change)

# Window_wahadlo.iconbitmap('c:\sddas')

## Frame LEWY
frame_left = tk.Frame(Window_wahadlo, padx=5, pady=5)
frame_left.grid(row=0, column=0, sticky='w')

##  (frama leego)
## ----- # górny frame "Górne wahadlo"
sq_frame1 = tk.LabelFrame(frame_left, width=100, padx=5, pady=5, text="Górne wahadlo")
sq_frame1.grid(row=0, column=0, sticky='w')
tk.Label(sq_frame1, text=f"Długość wahadła L1", padx=padx_label).grid(row=0, column=0, sticky='e')
tk.Label(sq_frame1, text=f"Kąt {chr(952)}1", padx=padx_label).grid(row=1, column=0, sticky='e')
tk.Label(sq_frame1, text="Masa M1", padx=padx_label).grid(row=2, column=0, sticky='e')

Entry_L1 = tk.Entry(sq_frame1, borderwidth=2, width=10)
Entry_L1.grid(row=0, column=1)
Entry_Th1 = tk.Entry(sq_frame1, borderwidth=2, width=10)
Entry_Th1.grid(row=1, column=1)
Entry_M1 = tk.Entry(sq_frame1, borderwidth=2, width=10)
Entry_M1.grid(row=2, column=1)


## ----- # dolny frame "Dolne wahadlo"
sq_frame2 = tk.LabelFrame(frame_left, padx=5, pady=5, text="Dolne wahadlo")
sq_frame2.grid(row=1, column=0, sticky='w')
tk.Label(sq_frame2, text=f"Długość wahadła L1", padx=padx_label).grid(row=0, column=0, sticky='e')
tk.Label(sq_frame2, text=f"Kąt {chr(952)}1", padx=padx_label).grid(row=1, column=0, sticky='e')
tk.Label(sq_frame2, text="Masa M1", padx=padx_label).grid(row=2, column=0, sticky='e')

Entry_L2 = tk.Entry(sq_frame2, borderwidth=2, width=10)
Entry_L2.grid(row=0, column=1)
Entry_Th2 = tk.Entry(sq_frame2, borderwidth=2, width=10)
Entry_Th2.grid(row=1, column=1)
Entry_M2 = tk.Entry(sq_frame2, borderwidth=2, width=10)
Entry_M2.grid(row=2, column=1)




# button_2 = tk.Button(sq_frame2)
# button_2.grid(row=0, column=0, sticky='n')

Window_wahadlo.mainloop()