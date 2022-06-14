import bmi.py as bmi

def get_advice(result):
    with open(f'{result}', encoding='utf-8') as porada:
        rada = porada.read()
    return rada

def get_value(message):
    while True:
        try:
            value = float(input(message))
        except (ValueError, TypeError) as err:
            print("Nieprawidłowa wartość!")
        else:
            return value

def main():
    w = get_value('Podaj wagę [kg]')
    h = get_value('Podaj wzrost(w metrach)')
    wynik = bmi.bmi(w, h)
    result = bmi.bmi_result(wynik)
    print(result)
    rada = get_advice(result)
    print(rada)


main()
