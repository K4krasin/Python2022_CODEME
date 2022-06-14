#  Stwórz listę 10 elementową (różne typy!).
#  Pozwól użytkownikowi podać dowolny index. Podziel 1 przez liczbę pod indexem wybranym przez użytkownika. Obsłuż błędy.

def get_index(list):
    list_index = int(input("Podaj index listy!: "))
    result = 1/list[list_index]
    return result



def main():
    list = [2, 'Gandalf', 24.41, 'Opos', '4 Pory Roku', 100, 0, {}, [1, 4], True, None]

    try:
        res = get_index(list)
        print(res)
    except TypeError:
            print(f'Pod podanym indexem nie znajduje się liczba')
    except ZeroDivisionError:
            print("Pod tym indexem znajduje się zero")
    except IndexError:
            print("Przekroczono długość listy. Podany index nie istnieje")
    except ValueError:
        print("Podany index nie jest liczbą naturalną")



if __name__ == "__main__":
    main()