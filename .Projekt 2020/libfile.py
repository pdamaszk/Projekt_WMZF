
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



