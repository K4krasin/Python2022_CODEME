# Utwórz listę, która zawiera składniki na ulubione danie.
# Wyświetl komunikaty co należy pokolei dodać. Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.


dish = ["Makaron", "Pomidory", "Pieczarki", "Ser żółty", "Bazylia"]
kol = 0

for i in dish:
    kol += 1
    print(f'-{kol} Dodaj', i)

print(f'Ugotuj {dish[0]}')
print(f'Poczekaj aż rozpuści się {dish[3]}')

# Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8).
print()
silnia = int(input("Podaj liczbę od 1 do 8: "))
wynik = silnia

for j in range(1, wynik, 1):
    wynik += wynik * (j - 1)


print(f'Silnia z {silnia} wynosi {wynik}')
