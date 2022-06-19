# Wywołaj błąd związany z otwarciem pliku.
#
# Spróbuj odczytać plik, który nie istnieje.
#
# Spróbuj odczytać wartość z pliku otwartym w trybie w
#
# Spróbuj utworzyć plik, który już istnieje w trybie x
#
# Obsłuż w dowolny sposób każdy z powyższych błędów.


def main():
    with open('file_dexist.txt', 'r') as f:
        try:
            f.read()
        except FileNotFoundError:
            f.readlines()

if __name__ == '__main__':
    main()