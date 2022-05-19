
hobbits = ["Pippin", "Merry", "Sam", "Voldemort"]
grades = [1, 2, 3 ,4 ,5]
hobbrades = hobbits + grades
print(hobbrades)

gr2 = grades.copy()
print(gr2)

hobbits.sort()
print(hobbits)

grades.clear()

lista = [1,2.3,2,4,2,7,2,2]
print(lista.count(2))
num_sum= sum(lista)
print(num_sum)

a = hobbits.count("Sam")

print()
print()

items = ["Jedenie", "Woda", "Raki", "Czapka", "Namiot"]
sorted_items = sorted(items)

for i in sorted_items:
    print('- ', i)


num = input("Podaj liczby oddzielone spacją: ")
num = num.split()
print(num)


if num[0] == num[-1]:
    print("Sa takie same")
else:
    print("Liczby się różnią")

####################


list_10 = []

new_input = int(input("Insert 10 numbers"))

for number in range(0, 10):
    new_number = int(input())
    list_10.append(new_number)

print(list_10)
print(list_10[0] == list_10[9])


# Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób, natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:
#
# Dorota, Wellman, dziennikarka
#
# Adam, Małysz, sportowiec
#
# Robert, Lewandowski, piłkarz
#
# Krystyna, Janda, aktorka
#
# Wyświetl w sposób przyjazny dla użytkownika

people = [

['Dorota', 'Wellman', 'dziennikarka'],
['Adam', 'Małysz', 'sportowiec'],
['Robert', 'Lewandowski', 'piłkarz'],
['Krystyna', 'Janda', 'aktorka'],
]

for p in people:
    for id, value in enumerate(p):
        if id == 1:
            print(value, end=' - ')
        else:
            print(value, end=' ')
    print()



