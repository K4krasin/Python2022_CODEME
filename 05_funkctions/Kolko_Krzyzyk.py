# Program będący implementacją gry w "kółko i krzyżyk" dla dwóch graczy. Wpisz w google "tic tac toe game" i zagraj z google.
#
# Zacznij od zaprojektowania rozgrywki
# Możliwość nazwania graczy inaczej niż X / O
# Rozszerzeniem gry będzie zmiana 2 gracza na komputer.
# Konieczność użycia modułu random.
# Przykładowo rozgrywka mogłaby wyglądać tak:

import random

tic_tac = ['-'] * 9


def player_choice(place):
    while tic_tac[place] != '-':
        print("miejsce zajete")
        place = int(input("Podaj liczbę odpowiadającą planszy (1 do 9): "))

    tic_tac[place - 1] = 'X'
    return tic_tac

def com_choice (ran_place):
    while tic_tac[ran_place] != '-':
        ran_place = random.randrange(0, 9)
    tic_tac[ran_place] = 'O'
    print(tic_tac)
    return tic_tac

def end_game(plansza):
    while True:
        if plansza[0:3] == 'X':
            print('Wygeywa gracz')
            return True
            break
        elif plansza[3:6] == 'X':
            print('Wygeywa gracz')
            return True
            break
        elif plansza[6:9] == 'X':
            print('Wygeywa gracz')
            return True
            break
        elif plansza[0] == plansza[3] == plansza[6] == 'X':
            print('Wygeywa gracz')
            return True
            break
        elif plansza[1] == plansza[4] == plansza[7] == 'X':
            print('Wygeywa gracz')
            return True
            break
        elif plansza[2] == plansza[5] == plansza[8] == 'X':
            print('Wygeywa gracz')
            return True
            break
        elif plansza[0] == plansza[4] == plansza[8] == 'X':
            print('Wygeywa gracz')
            return True
            break
        elif plansza[2] == plansza[4] == plansza[6] == 'X':
            print('Wygeywa gracz')
            return True
            break
        else:
            continue






def main():

    for _ in range(0,10):
        p1_choice = int(input("Podaj liczbę odpowiadającą planszy (1 do 9): "))
        player_choice(p1_choice)
        compchoice = random.randrange(1, 10)
        com_choice(compchoice)
        #end_game(tic_tac)
    print(tic_tac)

main()



'''
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


'''