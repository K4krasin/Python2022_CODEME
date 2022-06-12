# Stwórz moduł, który przechowuje wzór na deltę. Skorzystaj z wbudowanego modułu math. W nowym pliku wykorzystaj moduł.

from math import sqrt as pierw

def get_three_numbers():
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    c = int(input("Podaj c: "))
    delta = b ** 2 - 4 * a * c
    return delta, a, b, c

def find_zero (delta, a, b):
    if delta > 0:
        x1 = (-b + pierw(delta)) / 2 * a
        x2 = (-b - pierw(delta)) / 2 * a
        print(f'Miejsca zerowe funkcji to {x1} i {x2}')
        return x1, x2
    elif delta == 0:
        x0 = -b / 2 * a
        print(f'Miejsce zerowe funkcji to {x0}')
        return x0
    else:
        print("Delta mniejsza od zera. Obliczenia niewykonalne.")
