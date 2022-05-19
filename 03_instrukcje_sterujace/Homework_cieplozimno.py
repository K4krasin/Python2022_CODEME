# Stwórz grę ciepło zimno.
#
# Komputer losuje liczbę z zakresu od 1 do 100.
#
# Użytkownik podaje swój traf.
#
# Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
#
# Jeśli użytkownik zgadnie wygrywa gracz.
#
# Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.
import random
import cmath

comp =  random.randrange(1,100)
rounds = 6

for i in range(0,6):

    choice = int(input(f'Próba {i + 1}. Podaj liczbę od 1 do 100: '))

    if choice > 100 or (choice < 1):
        print("Miało byc od 1 do 100 :| Przegrywasz WALKOWEREM!!!! \n LOOOOSER \n LOOOOSER \n LOOOOSER \n LOOOOSER \n LOOOOSER \n LOOOOSER \n LOOOOSER")
        break

    if choice == comp:
        print("Wygrałeś")
        break

    elif abs(choice - comp) < 3:
        print("GORĄCOOOOOOO")

    elif abs(choice - comp) < 6:
        print("Bardzo ciepło!")

    elif abs(choice - comp) < 16:
        print("Ciepło!")

    elif abs(choice - comp) < 31:
        print("Zimno!")

    elif abs(choice - comp) < 51:
        print("Bardzo zimno!")

    else:
        print("Wrrrr... LODOWATO!!")

    if i == 5 and choice != comp:
        print(f'Niestety nie udało się wygrać... Szukaną liczbą była liczba {comp}.')





