# 2▹ Napisać funkcję, która sprawdza czy liczba jest parzysta.

#def even(number):
#    if number % 2 == 0:
#        return print("Liczba jest parzysta")
#    else:
#        return print("Nieparzysta")
#
#num = int(input("Podaj liczbę: "))
#even(num)

# 4▹ Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów (wykorzystać funkcje z pkt 2)

def even(even_number, new_even):
    for v in even_number:
        numb = v
        new_even.append(v)
        if v % 2 != 0:
            new_even.remove(v)
    return print(new_even)

num = [7, 4, 43, 7, 23, 5, 643, 56, 456546, 34563, 45634]
sec_ev = []
even(num, sec_ev)


# 4▹ Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie. Powinna zwrócić komunikat:
# “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.



