# Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie
# (np. secret_num = 5). Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

secret_num = 5
num = int(input("Podaj numer od 0 do 20: "))

while (secret_num != num):
    print("Spróbuj raz jeszcze")
    num = int(input("Podaj numer od 0 do 20: "))

print("TO JEST TEN NUMER")


# Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

txt = input("Podaj tekst:" )
lenght = len(txt)
print(txt[1:lenght:2])


for i in txt[1:lenght:2]:
    print(i)
# Mam wrażenie że to jakoś inaczej trzeba

##############################

# 4▹ Napisz grę - kamień (k) / papier (p) / nożyce (n).
#
# Użytkownik podaje jedną z 3 figur.
#
# Komputer losuje jedną z 3 figur.
#
# Sprawdź kto wygrał tę rundę.
#
# Zmień kod tak, by użytkownik mógł podac liczbę rund.
#
# Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
#
# Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

import random

round = int(input("Podaj ile rund chcesz zagrać: "))
comp_figure = ["K", "P", "N"]

comp_choise = random.choice(comp_figure)


score = 0
comp_score = 0


for i in range(0, round):

    figura = input("Wybierz jedno: Kamień(K), Papier(P), Nożyce(N): ")
    comp_choise = random.choice(comp_figure)
    print("Komputer wulosował: ", comp_choise)

    if figura != "K" and (figura != "P" and figura != "N"):
        comp_score += 1
        break

    if figura == comp_choise:
        print("Remis")


    elif figura == "K" and (comp_choise == "P"):
        print("Komp wygrał XD")
        comp_score += 1


    elif figura == "K" and (comp_choise == "N"):
        print("Wygrałeś :/")
        score += 1


    elif figura == "P" and (comp_choise == "N"):
        print("Komp wygrał XD")
        comp_score += 1


    elif figura == "P" and (comp_choise == "K"):
        print("Wygrałeś :/")
        score += 1


    elif figura == "N" and (comp_choise == "K"):
        print("Komp wygrał XD")
        comp_score += 1


    elif figura == "N" and (comp_choise == "P"):
        print("Wygrałeś :/")
        score += 1



    print("**********************")
    print(f'Twój wynik: {score}\nWynik komputera: {comp_score}')
    print("**********************")


if score > comp_score:
    print("**********************")
    print("Gratulacje! Pokonałeś komputer")

elif score < comp_score:
    print("**********************")
    print("Komputer z Tobą wygrał!")

else:
    print("**********************")
    print("Remis!")

###############################################
import random

round = int(input("Podaj do ilu ZWYCIĘSTW chcesz zagrać: "))
comp_figure = ["K", "P", "N"]

comp_choise = random.choice(comp_figure)

score = 0
comp_score = 0


while (round - 1 >= score and (round - 1 >= comp_score)):

    figura = input("Wybierz jedno: Kamień(K), Papier(P), Nożyce(N): ")
    comp_choise = random.choice(comp_figure)
    print("Komputer wylosował: ", comp_choise)

    if figura != "K" and (figura != "P" and figura != "N"):
        comp_score += 1
        print("**********************")
        print(f'Twój wynik: {score}\nWynik komputera: {comp_score}')
        print("**********************")
        continue

    if figura == comp_choise:
        print("Remis")


    elif figura == "K" and (comp_choise == "P"):
        print("Komp wygrał XD")
        comp_score += 1


    elif figura == "K" and (comp_choise == "N"):
        print("Wygrałeś :/")
        score += 1


    elif figura == "P" and (comp_choise == "N"):
        print("Komp wygrał XD")
        comp_score += 1


    elif figura == "P" and (comp_choise == "K"):
        print("Wygrałeś :/")
        score += 1


    elif figura == "N" and (comp_choise == "K"):
        print("Komp wygrał XD")
        comp_score += 1


    elif figura == "N" and (comp_choise == "P"):
        print("Wygrałeś :/")
        score += 1



    print("**********************")
    print(f'Twój wynik: {score}\nWynik komputera: {comp_score}')
    score = score
    comp_score = comp_score
    print("**********************")



if score > comp_score:
    print("**********************")
    print("Gratulacje! Pokonałeś komputer")

elif score < comp_score:
    print("**********************")
    print("Komputer z Tobą wygrał!")

else:
    print("**********************")
    print("Remis!")
