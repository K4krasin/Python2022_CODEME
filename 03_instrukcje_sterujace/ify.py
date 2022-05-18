season = "pizgawica"

if season == 'wiosna':
    print('zasadź rośliny')
elif season == 'lato':
    print('odpalaj browara')
elif season == 'jesien':
    print('zbierz owoce')
elif season == 'zima':
    print('brrr za zimno!')
else:
    print(f'nie ma takiej pory roku jak {season}')


# Poproś użytkownika o podanie liczby.
# Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty i wyświetl komunikat
# “Twoja liczba jest podzielna przez 3”.

number = int(input('Podaj liczbę :'))

if number % 3 == 0:
    print("Twoja liczba podzielna przez 3 :)")
else:
    print("Niestety Twoja liczba nie jest podzielna przez 3 :(")

# Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce.
# Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty.
# Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

fabula = float(input('Podaj ocenę fabuły w skali od 1 do 10:'))
bohaterowie = float(input('Podaj ocenę bohaterów w skali od 1 do 10:'))
miejsce_akcji = float(input('Podaj ocenę miejsca akcji w skali od 1 do 10:'))

srednia = (fabula + bohaterowie + miejsce_akcji)/3

if srednia > 7:
    print("Super książka")
elif srednia >= 5:
    print("przecietna")
else:
    print("nie warta uwagi")

# Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 dużą literę
# i mieć długość conajmniej 8 znaków. Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
# Wyświetl różne komunikaty w zależności od rodzaju błędu.

password = input("Podaj hasło: ")
if password.islower():
    print("Twoje hasło musi zawierać co najmniej jedną dużą literę")
if password.isupper():
    print("Twoje hasło musi zawierać co najmniej jedną małą literę")
if password.isalpha():
    print("Twoje hasło musi zawierać przynajmniej jedną liczbę")
if password.isdigit():
    print("Twoje hasło musi zawierać przynajmniej jedną litere")
if len(password) < 8:
    print("Twoje hasło musi zawierać minimum 8 znaków")


