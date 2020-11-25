# Rozkład liczby na czynniki pierwsze
from math import floor, sqrt

def sqrtE(x):
    return floor(sqrt(x))

x = 126
i = 2

czynniki = []
e = sqrtE(x)
while i <= e:
    # print(e)
    if x%i == 0:
        czynniki.append(i)
        x = x / i
        e = sqrtE(x)
    else:
        i += 1

czynniki.append(int(x))
print(f"Liczba {x} rozkłada sie na {czynniki}")
