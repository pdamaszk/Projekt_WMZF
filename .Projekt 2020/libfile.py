# --------------------------------------------------------------------
# ----------  Wczytywanie z klawiatury sprawdzenie poprawności--------
def czytaj_z_klawiatury(text, type='str'):
    x = (input(text))
    # if

    # if type == 'int':
    #     try:
    #         return x
    #     except:
    #         return False
    # if type == 'int':
    #     try:
    #         x = (input(text))
    #         return x
    #     except:
    #         return False

# --------------------------------------------------------------------
from colorama import Fore, Back, Style
from colorama import init
# from termcolor import colored
init()

print(Fore.RED + "Command >> ")  ## Red-colored print statement
# print(Style.RESET_ALL)   ## Reseting the colors back to default (so the input won't be red aswell)
print("\033[%d;%dH" % (1, 1))   ## Changing X and Y pos
inp = input()  ## Getting Input


# --------------------------------------------------------------------

# --------------------------------------------------------------------
# --------------------------------------------------------------------
def test_cursora01():
    import sys
    from colorama import Fore, Back, Style
    from colorama import init
    init()

    def printPos(x, y, text_to_print):   #Function that let us print in desired Position
        sys.stdout.write("\x1b[%d;%df%s" % (x, y, text_to_print))
        sys.stdout.flush()

    print(Fore.RED + "Command >>")   #Red-colored print statement
    printPos(1, 11, " ")   #Changing pos to 1, 11
    inp = input()    #Getting the input
    printPos(-1, 11, " ")   #Changing pos to 1, 11
    inp = input()    #Getting the input

# test_cursora01()


# --------------------------------------------------------------------
# --------------------------------------------------------------------
from ctypes import windll, Structure, c_long, byref


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]



def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}


# pos = queryMousePosition()
# print(pos)


# --------------------------------------------------------------------
# --------------------------------------------------------------------

# # import only system from os
# from os import system, name
#
# # import sleep to show output for some time period
# from time import sleep
#
#
# # define our clear function
# def clear():
#     # for windows
#     if name == 'nt':
#         _ = system('cls')
#
#         # for mac and linux(here, os.name is 'posix')
#     else:
#         _ = system('clear')
#
#     # print out some text
#
#
# print('hello geeks\n' * 10)
#
# # sleep for 2 seconds after printing output
# sleep(2)
#
# # now call function we defined above
# clear()
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# ----------  tworzenie nowego pliku ---------------------------------
def Nowyplik(path, plik, name=""):
    import datetime
    import os
    try:
        if name == "time":
            do_zmiany = plik.rsplit('.')
            wstaw = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
            wstaw = '_'+ wstaw + '_'
            plik = do_zmiany[0] + wstaw + "." + do_zmiany[1]
        open(os.path.join(path, plik), 'a').close()
        print("plik utworzony")
    except:
        print('Nie mogę utwotzyc pliku')
        pass
    return plik
# print(Nowyplik("", 'plik.py', 'time'))
# --------------------------------------------------------------------



