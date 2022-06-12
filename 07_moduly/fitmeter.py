import bmi

def get_advice(result):
    with open(f'{result}', encoding='utf-8') as porada:
        rada = porada.read()
    return rada


def main():
    dane = bmi.get_weight_high()
    wynik = bmi.bmi(dane[0], dane[1])
    result = bmi.bmi_result(wynik)
    print(result)
    rada = get_advice(result)
    print(rada)


main()