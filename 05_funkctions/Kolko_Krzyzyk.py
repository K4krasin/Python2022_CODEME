# Program będący implementacją gry w "kółko i krzyżyk" dla dwóch graczy. Wpisz w google "tic tac toe game" i zagraj z google.
#
# Zacznij od zaprojektowania rozgrywki
# Możliwość nazwania graczy inaczej niż X / O
# Rozszerzeniem gry będzie zmiana 2 gracza na komputer.
# Konieczność użycia modułu random.
# Przykładowo rozgrywka mogłaby wyglądać tak:

import random


list1 = ['-'] * 3
list2 = ['-'] * 3
list3 = ['-'] * 3


print(list1)
def player_move(choice_col, choice_row):
    if choice_col == 1:
        if list1[choice_row - 1] != '-':
            print("To miejsce jest zajęte")
        else:
            list1[choice_row - 1] = 'X'
    elif choice_col == 2:
        if list2[choice_row - 1] != '-':
            print("To miejsce jest zajęte")
        else:
            list2[choice_row - 1] = 'X'
    else:
        if list3[choice_row - 1] != '-':
            print("To miejsce jest zajęte")
        else:
            list3[choice_row - 1] = 'X'
    return list1, list2, list3

def com_move(comp_col, comp_row):
    if comp_col == 1:
        if list1[comp_row - 1] != '-':
            print("To miejsce jest zajęte")
        else:
            list1[comp_row - 1] = 'O'
    elif comp_col == 2:
        if list2[comp_row - 1] != '-':
            print("To miejsce jest zajęte")
        else:
            list2[comp_row - 1] = 'O'
    else:
        if list3[comp_row - 1] != '-':
            print("To miejsce jest zajęte")
        else:
            list3[comp_row - 1] = 'O'
    return list1, list2, list3


#player_col = int(input("Podaj kolumne(1:3): "))
#player_row = int(input("Podaj wiersz(1:3): "))

#compcol = random.randrange(1,3)
#comprow = random.randrange(1,3)

for _ in range(0,3):
    player_col = int(input("Podaj wiersz(1:3): "))
    player_row = int(input("Podaj kolumne(1:3): "))
    compcol = random.randrange(1,4)
    comprow = random.randrange(1,4)
    print(comprow, compcol)
    player_move(player_col,player_row)
    com_move(compcol,comprow)
    print(list1)
    print(list2)
    print(list3)


