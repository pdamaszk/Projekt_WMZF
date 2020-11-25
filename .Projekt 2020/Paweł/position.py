import time
import curses

def pbar(window):
    height, width = window.getmaxyx()
    for i in range(10):
        window.addstr(height -1, 0, "[" + ("=" * i) + ">" + (" " * (10 - i )) + "]")
        window.refresh()
        time.sleep(0.5)

curses.wrapper(pbar)