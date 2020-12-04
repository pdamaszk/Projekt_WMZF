def pull_icon(root,icon):
    root.iconbitmap(icon)
def canvas_X(x):
    return canvas_width // 2 + x
def canvas_Y(y):
    return canvas_height // 2 - y

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
    print(x1)
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

def create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)

def eventEnter(event):
    print(event.keysym)
    if event.keysym == "Return":
        checkvariables()
    # try:
    #     int(event.keysym)
    #     checkvariables()
    # except:
    #     pass

def checkvariables():

    try:
        L1 = float(Entry_L1.get())
    except:
        Entry_L1.delete(0, tk.END)
        messagebox.showwarning(title="Ostzreżenie", message="\tNiepoprawde długość ramienia górnego wahadła\t")
        Entry_L1.focus()
        return

    try:
        Th1 = float(Entry_Th1.get())

    except:
        Entry_Th1.delete(0, tk.END)
        messagebox.showwarning(title="Ostzreżenie", message="\tNiepoprawdy kąt górnego wahadła\t")
        Entry_Th1.focus()
        return

    try:
        L2 = float(Entry_L2.get())
    except:
        Entry_L2.delete(0, tk.END)
        messagebox.showwarning(title="Ostzreżenie", message="\tNiepoprawde długość ramienia dolnego wahadła\t")
        Entry_L2.focus()
        return
    try:
        Th2 = float(Entry_Th2.get())
        Calc_please(L1, Th1, L2, Th2)
    except:
        Entry_Th2.delete(0, tk.END)
        messagebox.showwarning(title="Ostzreżenie", message="\tNiepoprawdy kąt dolnego wahadła\t")
        Entry_Th2.focus()
        return
    if keypressed:
        try:
            M1 = float(Entry_M1.get())
        except:
            Entry_M1.delete(0, tk.END)
            messagebox.showwarning(title="Ostzreżenie", message="\tNiepoprawa wartość masy górnego wahadła\t")
            Entry_M1.focus()
            return
        try:
            M2 = float(Entry_M2.get())
        except:
            Entry_M2.delete(0, tk.END)
            messagebox.showwarning(title="Ostzreżenie", message="\tNiepoprawa wartość masy dolnego wahadła\t")
            Entry_M2.focus()
            return



# testowanie zawartosci okna
def test_interfecu():
    global test_id
    test_id = 1
