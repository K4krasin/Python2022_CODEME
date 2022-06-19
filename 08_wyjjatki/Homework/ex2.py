# Utwórz dowolną krotkę zawierającą kilka wartości np. 10. Pozwól użytkownikowi podać dowolny index oraz wartość.
# Spróbuj w krotce podmienić wartość na zadanym indeksie. Obsłuż błąd

def main():
    krot = (2, 6, 3, 'fs', True, None, [1, 4])

    krot_ind = int(input('Podaj index krotki: '))
    krot_wartosc = input("Podaj wartość krotki pod wskazanym indexem: ")

    if krot[krot_ind] != krot_wartosc:
        print("Czy chcesz zamienić? T/N")
        choice = input()
        choice = choice.upper()
        if choice == "T":
            lista = list(krot)
            lista[krot_ind] = krot_wartosc
            krot = tuple(lista)
            print(krot)
        else:
            print("Koniec")


if __name__ == '__main__':
    main()