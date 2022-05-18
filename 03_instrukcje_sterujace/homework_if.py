# Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
# Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

number1 = int(input('Podaj pierwszą liczbę całkowitą: '))
number2 = int(input('Podaj drugą liczbę całkowitą: '))

if number2 + number1 > 100:
    print("Koniec")
else:
    print("Próbuj dalej. Suma Twoich liczb musi być większa niż 100")

# Utwórz zmienną przechowującą dowolny ciąg znaków.
# Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

txt = input("Podaj dowolny ciąg znaków: ")

if len(txt) > 5 and (txt.count("a") >= 1):
    print("Ten ciąg znaków zawiera conajmniej jedną literę a.")

else:
    print("Ciąg zawiera mniej niż 5 znaków bądź nie posiada litery 'a'")

if txt.isalpha():
    txt = txt.replace("a", "z")
    print(txt)
else:
    print("Ciąg znaków jest złożony nie tylko z liter.")



# Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę
# wyświetl komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.

num = int(input("Podaj ukrytą liczbę z zakresu od 1 do 100: "))

if num == 48:
    print("Gratulacje!")
else:
    print("Pudło")


# Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową,
# która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.

W = float(input('Podaj wagę:'))
H = float(input('Podaj wzrost (w metrach):'))


BMI = W/(H ** 2)
BMI = round(BMI, 2)

print()

print("your BMI is:", round(W/(H ** 2), 2))

if BMI < 16:
    print("Wygłodzenie!")

elif BMI < 17:
    print("Wychudznie!")

elif BMI < 18.50:
    print("Niedowaga!")

elif BMI < 25:
    print("Pożądana masa ciała!")

elif BMI < 30:
    print("Nadwaga!")

elif BMI < 35:
    print("Otyłość 1 stopnia!")

elif BMI < 40:
    print("Otyłość II stopnia!")

elif BMI >= 40:
    print("Otyłość III stopnia!")


# Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

num1 = float(input("Podaj pierwszą dowolną liczbę:"))
num2 = float(input("Podaj drugą dowolną liczbę:"))
num3 = float(input("Podaj trzecią dowolną liczbę:"))

Najw = 0
Srednia = 0
Najm = 0

if num1 > num2 and (num1 > num3):
    Najw = num1

elif num1 > num2 or ((num1 > num3) and ((num1 < num2) or (num1 < num3))):
    Srednia = num1

elif num1 < num2 and (num1 < num3):
    Najm = num1

#######################################

if num2 > num1 and (num2 > num3):
    Najw = num2

elif num2 > num1 or ((num2 > num3) and ((num2 < num1) or (num2 < num3))):
    Srednia = num2

elif num2 < num1 and (num2 < num3):
    Najm = num2

#######################################

if num3 > num2 and (num3 > num1):
    Najw = num3

elif num3 > num2 or ((num3 > num1) and ((num3 < num2) or (num3 < num1))):
    Srednia = num3

elif num3 < num2 and (num3 < num1):
    Najm = num3

#######################################


if num1 == num2 and (num2 > num3):
    Najw = num1
    Srednia = num2
    Najm = num3

elif num1 == num2 and (num2 < num3):
    Najw = num3
    Srednia = num2
    Najm = num2

elif num1 == num3 and (num1 < num2):
    Najw = num2
    Srednia = num1
    Najm = num1

elif num1 == num3 and (num1 > num2):
    Najw = num1
    Srednia = num1
    Najm = num2

elif num1 > num2 and (num2 == num3):
    Najw = num1
    Srednia = num2
    Najm = num2

elif num1 < num2 and (num2 == num3):
    Najw = num2
    Srednia = num2
    Najm = num1

else:
    Najw = Najm = Srednia = num1

print()
print(f'Największa {Najw}\nŚrednia {Srednia} \nNajmniejsza {Najm}')
