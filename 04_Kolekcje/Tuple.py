''''
siersciuch = ('Kot', 'Dachowiec', 'Mruczka')
(zwierze, rasa, imie) = siersciuch

print(f'Mój {zwierze} jest rasy {rasa} i nazywa się {imie}')

# Stwórz krotkę liczb całkowitych. Poproś użytkownika o podanie dowolnej liczby. Jeśli liczba znajduje się na krotce wyswietl jej indeks.

numbers = (1, 3, 4, 20, 13, 16, 9)

num = input("Podaj liczbę od 1 do 20 ->")
flag = False

for i, v in enumerate(numbers):
    if int(num) == v:
        print('znalazłem, pod indexem:', i)
        flag = True
        break

if not flag:
    print('nie ma takiej liczby')

'''
#  Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki,
#  a oraz nieparzystych elementów z drugiej. Przekształć powstałą listę w set.

krot1 = (1,5,2,6,346,23,56,2,6)
krot2 = (23,535,35,3,53,55,4,54,3,43,5435,3)

lista = list(krot1[::2] + krot2[1::2])
print(lista)
result = set(lista)
print(result)






