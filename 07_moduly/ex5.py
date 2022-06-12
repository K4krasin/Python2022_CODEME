# Stwórz moduł obliczający pola różnych figur.
# W nowym pliku utwórz skrypt, który na podstawie podanych składowych kształtów pomieszczeń oraz ich wymiarów zwraca powierzchnię budynku.


def check_figure():
    fig = input("Wybierz figure do obliczenia (K - Kwadrat, P - prostokąt, T - Trójkąt, O - Okrąg: ")
    fig = fig.upper()
    return fig

def select_method(fig):
    if fig == 'K':
        a = int(input("Podaj wymiar ściany kwadratu: "))
        return a*a
    elif fig == 'P':
        a = int(input("Podaj wymiar ściany prostokatu: "))
        b = int(input("Podaj wymiar ściany prostokatu: "))
        return a*h/2
    elif fig == 'T':
        a = int(input("Podaj wymiar podstawy trojkatu: "))
        h = int(input("Podaj wysokość trójkąta: "))
        return a*h/2
    else:
        r = int(input("Podaj promień koła: "))
        return 3.14*r*r

def add_another_shape():






