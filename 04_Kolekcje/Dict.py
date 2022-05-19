# Utwórz listę lists_to_dict zawierającą listy 2 elementowe. Przekształć ją w słownik dict_from_list.
''''
list_to_dict = [
    ["key", "value"],
    ['lech', 'mistrz'],
    ["cat", "chat"]
]

dict_from_list = dict(list_to_dict)
print(dict_from_list)

# Utwórz dowolną tablicę n x n zawierającą dowolny znak, a następnie wyświetl jej elementy w formie tabeli n x n.
# Elementy powinny być oddzielone spacją

n = int(input("Liczba: "))

tab = [['-'] * n] * n

for t in tab:
    for id, value in enumerate(t):
        if id == 1:
            print(value, end=' ')
        else:
            print(value, end=' ')
    print()
'''
# W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.

txt = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""





days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}

val = days.values()
print(list(set(val)))


#  Użytkownik podaje dowolną liczbę N. Napisz, który wygeneruje słownik, wg zasady, że każdej liczbie przyporządkowany jest jej kwadrat (n : n * n).
#
# Załóżmy, że użytkownik podał N = 8
#
# Wynik: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

n = int(input("Podaj liczba od 1 do 10: "))
dict_sqr = {}

for v in range(1, n + 1):
    dict_sqr[v] = v * v

print(dict_sqr)



