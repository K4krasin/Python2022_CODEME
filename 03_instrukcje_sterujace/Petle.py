
# Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry.
# Wyświetl nazwę właśnie spakowanego przedmiotu, po ostatnim przedmiocie pokaż informację: “Great, we are ready!”

items = ["raki", "czapka", "woda"]
for i in items:
    print('- ',i)

print("Great, we are ready!")

# Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
# Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
suma = 0

for i in range(1,11):
    suma += i
    print(suma)

##########

price = 15

while(price > 10):
    print(price, "Za drogo!")
    price = price - 2

print(price, "gitara")


# 1) Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
# Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
#
# C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit
#
# Napisz rozwiązanie zarówno z użyciem pętli while jak i for.

F = 0
C = 5/9*(F-32)

while(F <= 200):
    C = 5 / 9 * (F - 32)
    print(f'{F} st F -> {round(C, 1)} st C')
    F += 20

#for st in range(F,200,F+20):
#    C = 5 / 9 * (F - 32)
#    print(f'{F} st F -> {round(C, 1)} st C')



for val in "string":
  if val == "i":
      break
  print(val)

print("Koniec")


subject = "Przedmiot"
grade = "ocena"
sum_grades = 0

for i in range(0,3):
    subject = input("Podaj nazwe :")
    grade = int(input("Podaj ocene :"))
    print(f'Ocena z {subject} to {grade}')
    sum_grades += grade




#Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem
# (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem). Następnie powitaj każdą osobę na liście.



names = "Ada, Michał, Jacek"
names = names.split(', ')

for name in names:
    print("Hello!", names)



#3▹ W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.

txt = "aBarKadabra123"
ml = 0
wl = 0
c = 0
zs = 0

for t in txt:

    if t.islower():
        ml += 1
        continue

    if t.isupper():
        wl += 1
        continue

    if t.isdigit():
        c += 1

print(ml, wl, c)