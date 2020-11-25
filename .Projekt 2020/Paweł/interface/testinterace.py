
def tkinter001():
    import tkinter as tk

    def startgame():

        pass

    mw = tk.Tk()

    #If you have a large number of widgets, like it looks like you will for your
    #game you can specify the attributes for all widgets simply like this.
    mw.option_add("*Button.Background", "black")
    mw.option_add("*Button.Foreground", "red")

    mw.title('Wahadlo Balistyczne')
    #You can set the geometry attribute to change the root windows size
    mw.geometry("800x500") #You want the size of the app to be 500x500
    mw.resizable(1, 1) #Don't allow resizing in the x or y direction

    back = tk.Frame(master=mw,bg='#444444')
    back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
    back.pack(fill=tk.BOTH, expand=1) #Expand the frame to fill the root window

    #Changed variables so you don't have these set to None from .pack()
    go = tk.Button(master=back, text='Start Game', command=startgame)
    go.pack()
    close = tk.Button(master=back, text='Quit', command=mw.destroy)
    close.pack()
    info = tk.Label(master=back, text='Made by me!', bg='red', fg='black')
    info.pack()

    mw.mainloop()

#todo -----------------------text box
def tkinter002():
    import tkinter as tk

    root = tk.Tk()
    T = tk.Text(root, height=2, width=30)
    T.pack()
    T.insert(tk.END, "Just a text Widget\nin two lines\n")
    tk.mainloop()

#todo -----------------------2 text boxes
def tkinter003():
    import tkinter as tk
    import random
    import timeit

    class TextWithVar(tk.Text):
        '''A text widget that accepts a 'textvariable' option'''

        def __init__(self, parent, *args, **kwargs):
            try:
                self._textvariable = kwargs.pop("textvariable")
            except KeyError:
                self._textvariable = None

            tk.Text.__init__(self, parent, *args, **kwargs)

            # if the variable has data in it, use it to initialize
            # the widget
            if self._textvariable is not None:
                self.insert("1.0", self._textvariable.get())

            # this defines an internal proxy which generates a
            # virtual event whenever text is inserted or deleted
            self.tk.eval('''
                proc widget_proxy {widget widget_command args} {

                    # call the real tk widget command with the real args
                    set result [uplevel [linsert $args 0 $widget_command]]

                    # if the contents changed, generate an event we can bind to
                    if {([lindex $args 0] in {insert replace delete})} {
                        event generate $widget <<Change>> -when tail
                    }
                    # return the result from the real widget command
                    return $result
                }
                ''')

            # this replaces the underlying widget with the proxy
            self.tk.eval('''
                rename {widget} _{widget}
                interp alias {{}} ::{widget} {{}} widget_proxy {widget} _{widget}
            '''.format(widget=str(self)))

            # set up a binding to update the variable whenever
            # the widget changes
            self.bind("<<Change>>", self._on_widget_change)

            # set up a trace to update the text widget when the
            # variable changes
            if self._textvariable is not None:
                self._textvariable.trace("wu", self._on_var_change)

        def _on_var_change(self, *args):
            '''Change the text widget when the associated textvariable changes'''

            # only change the widget if something actually
            # changed, otherwise we'll get into an endless
            # loop
            text_current = self.get("1.0", "end-1c")
            var_current = self._textvariable.get()
            if text_current != var_current:
                self.delete("1.0", "end")
                self.insert("1.0", var_current)

        def _on_widget_change(self, event=None):
            '''Change the variable when the widget changes'''
            if self._textvariable is not None:
                self._textvariable.set(self.get("1.0", "end-1c"))

    class Example(tk.Frame):
        def __init__(self, parent):
            tk.Frame.__init__(self, parent)

            self.textvar = tk.StringVar()
            self.textvar.set("Hello, world!")

            # create an entry widget and a text widget that
            # share a textvariable; typing in one should update
            # the other
            self.entry = tk.Entry(self, textvariable=self.textvar)
            self.text = TextWithVar(self, textvariable=self.textvar,
                                    borderwidth=1, relief="sunken",
                                    background="bisque")

            self.entry.pack(side="top", fill="x", expand=True)
            self.text.pack(side="top", fill="both", expand=True)

    if __name__ == "__main__":
        root = tk.Tk()
        Example(root).pack(fill="both", expand=True)
        root.mainloop()
    return 0

#todo -----------------------_
# def tkinter004():
#     from tkinter import Frame, Variable, Scrollbar, Text
#
#     from tkinter.constants import VERTICAL, RIGHT, LEFT, BOTH, END, Y
#
#     class TextExtension(Frame):
#         """Extends Frame.  Intended as a container for a Text field.  Better related data handling
#         and has Y scrollbar."""
#
#         def __init__(self, master, textvariable=None, *args, **kwargs):
#
#             super(TextExtension, self).__init__(master)
#             # Init GUI
#
#             self._y_scrollbar = Scrollbar(self, orient=VERTICAL)
#
#             self._text_widget = Text(self, yscrollcommand=self._y_scrollbar.set, *args, **kwargs)
#             self._text_widget.pack(side=LEFT, fill=BOTH, expand=1)
#
#             self._y_scrollbar.config(command=self._text_widget.yview)
#             self._y_scrollbar.pack(side=RIGHT, fill=Y)
#
#             if textvariable is not None:
#                 if not (isinstance(textvariable, Variable)):
#                     raise TypeError("tkinter.Variable type expected, " + str(type(textvariable)) + " given.".format(
#                         type(textvariable)))
#                 self._text_variable = textvariable
#                 self.var_modified()
#                 self._text_trace = self._text_widget.bind('<<Modified>>', self.text_modified)
#                 self._var_trace = textvariable.trace("w", self.var_modified)
#
#         def text_modified(self, *args):
#             if self._text_variable is not None:
#                 self._text_variable.trace_vdelete("w", self._var_trace)
#                 self._text_variable.set(self._text_widget.get(1.0, END))
#                 self._var_trace = self._text_variable.trace("w", self.var_modified)
#                 self._text_widget.edit_modified(False)
#
#         def var_modified(self, *args):
#             self.set_text(self._text_variable.get())
#             self._text_widget.edit_modified(False)
#
#         def unhook(self):
#             if self._text_variable is not None:
#                 self._text_variable.trace_vdelete("w", self._var_trace)
#
#         def clear(self):
#             self._text_widget.delete(1.0, END)
#
#         def set_text(self, _value):
#             self.clear()
#             if (_value is not None):
#                 self._text_widget.insert(END, _value)
#     return 0

#todo -----------------------_
def tkinter005():
    import tkinter as tk

    def function(text):
        print(text)

    root = tk.Tk()

    buttons = []

    for txt in ('Yes', 'No'):
        # problem: all buttons will print "No"
        # b = tk.Button(root, text=txt, command=(lambda:function(txt)))

        b = tk.Button(root, text=txt, command=(lambda x=txt: function(x)))
        b.pack()
        buttons.append(b)

    root.mainloop()


#todo -----------------------_
def tkinter006():
    import tkinter as tk

    def write_slogan():
        print("Tkinter is easy to use!")

    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    button = tk.Button(frame,
                       text="QUIT",
                       fg="red",
                       command=quit)
    button.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                       text="Hello",
                       command=write_slogan)
    slogan.pack(side=tk.LEFT)

    root.mainloop()
    return 0

#todo -----------------------_
def tkinter007():
    import tkinter as tk

    def show_entry_fields():
        print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

    master = tk.Tk()
    master.geometry("800x600")
    master.title('Wahadlo Balistyczne')
    tk.Label(master,
             text="First Name").grid(row=0)
    tk.Label(master,
             text="Last Name").grid(row=1)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    tk.Button(master,
              text='Quit',
              command=master.quit).grid(row=3,
                                        column=0,
                                        sticky=tk.W,
                                        pady=4)
    tk.Button(master,
              text='Show', command=show_entry_fields).grid(row=3,
                                                           column=1,
                                                           sticky=tk.W,
                                                           pady=4)

    tk.mainloop()
    return 0
#todo -----------------------formularz
def tkinter008():
    import tkinter as tk

    fields = 'Last Name', 'First Name', 'Job', 'Country'

    def fetch(entries):
        for entry in entries:
            field = entry[0]
            text = entry[1].get()
            print('%s: "%s"' % (field, text))

    def makeform(root, fields):
        entries = []
        for field in fields:
            row = tk.Frame(root)
            lab = tk.Label(row, width=15, text=field, anchor='w')
            ent = tk.Entry(row)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            entries.append((field, ent))
        return entries

    if __name__ == '__main__':
        root = tk.Tk()
        ents = makeform(root, fields)
        root.bind('<Return>', (lambda event, e=ents: fetch(e)))
        b1 = tk.Button(root, text='Show',
                       command=(lambda e=ents: fetch(e)))
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        b2 = tk.Button(root, text='Quit', command=root.quit)
        b2.pack(side=tk.LEFT, padx=5, pady=5)
        root.mainloop()
    return 0

#todo -----------------------form 2
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
                                                                   sticky=tk.W,
                                                                   pady=4)

    master.mainloop()

    tk.mainloop()

#todo -----------------------math form
def tkinter010():
    import tkinter as tk

    fields = ('Annual Rate', 'Number of Payments', 'Loan Principle', 'Monthly Payment', 'Remaining Loan')

    def monthly_payment(entries):
        # period rate:
        r = (float(entries['Annual Rate'].get()) / 100) / 12
        print("r", r)
        # principal loan:
        loan = float(entries['Loan Principle'].get())
        n = float(entries['Number of Payments'].get())
        remaining_loan = float(entries['Remaining Loan'].get())
        q = (1 + r) ** n
        monthly = r * ((q * loan - remaining_loan) / (q - 1))
        monthly = ("%8.2f" % monthly).strip()
        entries['Monthly Payment'].delete(0, tk.END)
        entries['Monthly Payment'].insert(0, monthly)
        print("Monthly Payment: %f" % float(monthly))

    def final_balance(entries):
        # period rate:
        r = (float(entries['Annual Rate'].get()) / 100) / 12
        print("r", r)
        # principal loan:
        loan = float(entries['Loan Principle'].get())
        n = float(entries['Number of Payments'].get())
        monthly = float(entries['Monthly Payment'].get())
        q = (1 + r) ** n
        remaining = q * loan - ((q - 1) / r) * monthly
        remaining = ("%8.2f" % remaining).strip()
        entries['Remaining Loan'].delete(0, tk.END)
        entries['Remaining Loan'].insert(0, remaining)
        print("Remaining Loan: %f" % float(remaining))

    def makeform(root, fields):
        entries = {}
        for field in fields:
            print(field)
            row = tk.Frame(root)
            lab = tk.Label(row, width=22, text=field + ": ", anchor='w')
            ent = tk.Entry(row)
            ent.insert(0, "0")
            row.pack(side=tk.TOP,
                     fill=tk.X,
                     padx=5,
                     pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT,
                     expand=tk.YES,
                     fill=tk.X)
            entries[field] = ent
        return entries

    if __name__ == '__main__':
        root = tk.Tk()
        ents = makeform(root, fields)
        b1 = tk.Button(root, text='Final Balance',
                       command=(lambda e=ents: final_balance(e)))
        b1.pack(side=tk.LEFT, padx=5, pady=5)
        b2 = tk.Button(root, text='Monthly Payment',
                       command=(lambda e=ents: monthly_payment(e)))
        b2.pack(side=tk.LEFT, padx=5, pady=5)
        b3 = tk.Button(root, text='Quit', command=root.quit)
        b3.pack(side=tk.LEFT, padx=5, pady=5)
        root.mainloop()
    return 0

#todo -----------------------_
from tkinter import *
from tkinter.filedialog import askopenfilename

def tkinter011():

    def NewFile():
        print("New File!")

    def OpenFile():
        name = askopenfilename()
        print(name)

    def About():
        print("This is a simple example of a menu")

    root = Tk()
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New", command=NewFile)
    filemenu.add_command(label="Open...", command=OpenFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)

    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=About)

    mainloop()
    return 0
#todo -----------------------_
def tkinter126():

    return 0

tkinter009()
