# Oblicz średnią arymetyczną z kilku liczb. Liczby będą podane przez użytkownika po przecinku. Napisz funkcję, która przyjmie wartości i wyświetli średnią.
# Program powinen być odporny na błędy użytkownika. Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.
import math

def get_numbers():
    numbers = []
    choice = 'T'
    while choice == 'T':
        try:
            num = float(input("Podaj liczbę: "))
        except ValueError:
            with open('Errors', 'a', encoding='UTF-8') as f:
                f.write(f'Value error \n')
        except TypeError:
            with open('Errors', 'a', encoding='UTF-8') as f:
                f.write('Type error')
        else:
            numbers.append(num)
        print('Czy chcesz podac kolejną liczbę? T/N')
        choice = input()
        choice = choice.upper()
    return numbers


def calc_avarange(numbers):
    lenght = len(numbers)
    suma = 0

    for i in range(0,lenght):
        suma += numbers[i]
    print(f'suma całkowita wynosi: {suma}')
    avarange = round(suma/lenght, 2)
    return avarange


def main():

    numbers = get_numbers()
    print(numbers)
    print(calc_avarange(numbers))

if __name__ == '__main__':
    main()