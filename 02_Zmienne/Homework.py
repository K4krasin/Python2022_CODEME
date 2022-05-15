
# Czy 43 - 13 będzie się równać 11 + 12 ?
print(43 - 13 == 11 + 12)

#Czy dzielenie 129 przez 17 bez reszty wynosi 3?
print(129 // 13 == 3)

#Czy 247 podzielone przez 5 daje resztę 2?
print(247 % 5 == 2)

#Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = input('Podaj pierwszy wyraz: ')
s2 = input('Podaj drugi wyraz: ')
half = len(s2)//2
s3 = s2[:half] + s1 + s2[half:]
print(s3)

#Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:

#  - Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.

#  - Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich

#  - Połącz dane w jeden ciąg book za pomocą spacji

#  - liczbę wszystkich znaków w napisie book


title = input('Podaj tytuł książki: ')
autor = input('Podaj nazwiasko autora książki: ')
pages = input('Podaj liczbę stron: ')

check_title = title.isalnum()
check_pages = pages.isnumeric()
print(f'Czy tytuł {title} składa się z samych liter oraz strony są podane jako liczba -> ',check_title, check_pages)

print("Nazwisko autora :", autor.title())

book = title + " " + autor + " " + pages
ilosc_znakow = len(book)
print('liczba znaków w napisie book jest równa: ', ilosc_znakow)


# Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej
# np.: Kobyła ma mały bok. Pozwól użytkownikowi wprowadzić dowolne zdanie.
# Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.


palindrom = input('Podaj palindrom: ')
palindrom = palindrom.replace(" ","")
palindrom = palindrom.lower()

print(f'Podany wyraz: {palindrom} jest palindronem ->', palindrom == palindrom[::-1])



# Przekopiuj zawartość import this do zmiennej.

it = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""


# Policz liczbę wystąpień słowa better.

print('W import this znajduje sie następująca liczba słowa better:', it.count("better"))

# Usuń z tekstu symbol gwiazdki

it.strip('*')

# Zamień jedno wystąpienie explain na understand

print(it.replace("explain", "understand" , 1))

# Usuń spacje i połącz wszystkie słowa myślnikiem

print(it.replace(" ", "-"))

# Podziel tekst na osobne zdania za pomocą kropki

print(it.split('.'))

# Stwórz dwie dowolne zmienne przechowujące wartość liczbową i tekstową. Użyj funkcji format(),
# by wyświetlić zdanie zawierające te wartości.

date = "14 maja"
num = 8
print(" Lech Poznań zdobył w dniu {} mistrzostwo Polski po raz {} w historii".format(date, num))

