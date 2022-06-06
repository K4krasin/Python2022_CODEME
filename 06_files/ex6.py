# Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.
# Co wiemy o tych numerach tych kart?
#
# All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
# MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
# American Express card numbers start with 34 or 37 and have 15 digits.

def is_card(number):
    return number.isdigit() and 13 <= len(number) <= 16


def is_visa(number):
    return len(number) in [13, 16] and number[0] == '4'


def is_mastercard(number):
    if len(number) == 16 and (51 <= int(number[0:2]) <= 55 or int(number[0:4]) in range(2221, 2720 + 1)): # 2720 + 1 -> bo range (start do end = n+1)
        return True
    else:
        return False

def check_card(number):
    if is_visa(number):
        save('visa', number)
    elif is_mastercard(number):
        save('mastercard', number)
    elif is_american_express(number):
        save('amex', number)
    else:
        save('unknown_card', number)

def is_american_express(number):
    return len(number) == 15 and number.startswith(('34', '37'))

def read():
    with open('cards_numbers', encoding='utf-8') as fopen:
        numbers = fopen.readlines()
    return numbers


def save(cardtype, number):
    with open(f'{cardtype}.txt', 'a') as fopen:
        fopen.write(f'{number}\n')

def main():

    cards_list = read()

    for number in cards_list:
        number = number.replace(' ', '').replace('\n', '')
        check_card(number)

    print('Karty zostały podzielone na pliki')

main()