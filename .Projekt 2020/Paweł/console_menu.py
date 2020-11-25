
# todo ---------- clear terminal screen
def clearscreen():
    from os import system, name

    if name == 'nt':
        _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# todo ---------- color & move
def test002():
    import sys
    from colorama import Fore, Back, Style
    from colorama import init
    init()

    def printPos(x, y, text_to_print):  # Function that let us print in desired Position
        sys.stdout.write("\x1b[%d;%df%s" % (x, y, text_to_print))
        sys.stdout.flush()
        sys.stdin.read()
    print(Fore.RED + "Command >>")  # Red-colored print statement
    printPos(1, 11, " ")  # Changing pos to 1, 11
    inp = input()  # Getting the input

# todo ---------- move in terminal & print
def printPos(x, y, text_to_print):  # Function that let us print in desired Position
    import sys
    from colorama import init
    init()
    sys.stdout.write("\x1b[%d;%df%s" % (x, y, text_to_print))
    sys.stdout.flush()


# todo ---------- read key
def readkey():
    from msvcrt import getch
    while True:
        key = getch()
        print(key)

# todo ---------- key detect
def keydetekt():
    from pynput.keyboard import Key, Listener
    word = ""
    def on_press(key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
        except AttributeError:
            print('special key {0} pressed'.format(
                key))

    def on_release(key):
        print('{0} release'.format(
            key))
        if key == Key.esc:
            # Stop listener
            return False

    # Collect events until released
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# todo ---------- key detect v2
def det():
    from pynput import keyboard

    with keyboard.Events() as events:
        for event in events:
            if event.key == keyboard.Key.esc:
                break
            else:
                print('Received event {}'.format(event))

# todo ---------- global key activation
def global_key():
    from pynput import keyboard

    def on_activate():
        print('Global hotkey activated!')

    def for_canonical(f):
        return lambda k: f(l.canonical(k))

    hotkey = keyboard.HotKey(
        keyboard.HotKey.parse('<ctrl>+<alt>+h'),
        on_activate)
    with keyboard.Listener(
            on_press=for_canonical(hotkey.press),
            on_release=for_canonical(hotkey.release)) as l:
        l.join()

# todo ---------- colors
def colors():
    print (u"\u001b[31mHelloWorld")
    print (u"\u001b[30;1m A \u001b[31;1m B \u001b[32;1m C \u001b[33;1m D \u001b[0m")
    print (u"\u001b[34;1m E \u001b[35;1m F \u001b[36;1m G \u001b[37;1m H \u001b[0m")


    import sys
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
        print(u"\u001b[0m")
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))

        print(u"\u001b[0m")
        # todo           tło niebieskie     :   \u001b[48;5;18m
        # todo      czcionka zolty          :   \u001b[38;5;11m
        # todo               Underline      :   \u001b[4m
        # todo               BOLD           :   \u001b[1m

    print(u"\u001b[48;5;18m\u001b[38;5;11m\u001b[4m\u001b[1m BOLD")
    print(u"\u001b[1m\u001b[4m\u001b[7m BOLD Underline Reversed \u001b[0m")
    print(u"\u001b[1m\u001b[31m Red Bold \u001b[0m")
    print(u"\u001b[4m\u001b[44m Blue Background Underline \u001b[0m")









