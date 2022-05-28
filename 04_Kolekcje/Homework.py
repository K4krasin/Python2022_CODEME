''''
# 2▹ Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
list10 = []
listnp = []

num = int(input("Insert 10 numbers: "))

for number in range(0, 10):
    num = int(input())
    list10.append(num)
    if num % 2 != 0:
        listnp.append(num)

print(listnp)
# 4▹ Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same


lits = []
el = 0

for elem in range(0, 10):
    el = input("Dawaj jakiś element: ")
    lits.append(el)

print(lits)
dlugosc = len(lits)
if lits[4] == lits[5]:
    print("Są równe")
else:
    print("Nie są równe")

# 2▹ Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.

lm_winners = ("Zaksa", "Zaksa", "Lube", "Zenit", "Zenit", "Zenit", "Zenit", "Biełgorje")
powt_tup = []

for i, ele in enumerate(lm_winners):
    if lm_winners.count(ele) > 1:
        powt_tup.append((ele))
        print("to nie adziala", i, ele)
    else:
        print("nie zadziala")

powt_set = set(powt_tup)
print(powt_set)
#print(powt_set)

# 1▹ Utwórz dowolną krotkę, w której elementy mogą się powtarzać. Przekształć ją w set.

tup_random = ('Punto', 'Yaris', 'Panda', 'Punto', 'Verso', 'Verso')
tup_random_set = set(tup_random)

print(tup_random_set)


# 4▹ Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.

long_list = ['BMW', 'Audi', 'Fiat', 'e90', 'A3', 'Punto', 2004, 2010, 2011]
len_of_list = len(long_list)
av_list = int(len_of_list/3)

print(len_of_list, av_list)
list_of3 = [
    [long_list[0:av_list]],
    [long_list[av_list:av_list*2]],
    [long_list[av_list*2:av_list*3]]
    ]
print(list_of3)

# 5▹ Porównaj zachowanie discard() vs remove() dla typu set.


# 2▹ Utwórz listę lub krotkę tuples_to_dict zawierającą krotki 2 elementowe. Przekształć ją w słownik dict_from_tuples

tuples_to_dict = [
    ("key", "value"),
    ('LECH', 'Mistrz!'),
    ("cat", "chat")
]

dict_from_tuple = dict(tuples_to_dict)
print(dict_from_tuple)

'''
# 4▹ Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10, wypełnioną wynikami mnożenia wiersz × kolumna.

num = 0
mult_tab = [[] * 10] * 10
multiply_tab = []
for i in range(0, 10):
    for j in range(0, 10):
        num = i * j
        multiply_tab.append([])
        mult_tab.append(num)
        #tab_mnoz = tab_mnoz.append([num])





# 6▹ Utwórz listę zawierającą wartości poniższego słownika, bez duplikatów.

days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}

lbd = list(days.keys())
lbd2 = list(set(days.values()))
list_from_dic = lbd + lbd2
print(list_from_dic)


# 7▹ Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce.

example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
set_from_list = set(example_list)
tup_from_set = tuple(set_from_list)
print(tup_from_set)
print(max(tup_from_set), min(tup_from_set))

#  8▹ Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych imion żeńskich.
#  Zapisz imiona w wersji anglojęzycznej.
#  Dodaj wszystki listy razem. Nowa lista powinna zawierać 100 elementów.
# Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.



# 9▹ 5 użytkowników poproś o podanie 4 przedmiotów szkolnych,
# sprawdź czy przedmioty powtarzają się na listach. Wyświetl najpopularniejszy przedmiot.
# (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi, drukowanymi lub zaczynając od dużej litery)
