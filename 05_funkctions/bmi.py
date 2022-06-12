def bmi(waga, wzrost):
    return round(waga/wzrost ** 2,2)

def bmi_result(bmi_res):
    if bmi_res < 16:
        return ("Wygłodzenie!")

    elif bmi_res < 17:
        return ("Wychudznie!")

    elif bmi_res < 18.50:
        return ("Niedowaga!")

    elif bmi_res < 25:
        return ("Pożądana masa ciała!")

    elif bmi_res < 30:
        return ("Nadwaga!")

    elif bmi_res < 35:
        return ("Otyłość 1 stopnia!")

    elif bmi_res < 40:
        return ("Otyłość II stopnia!")

    elif bmi_res >= 40:
        return ("Otyłość III stopnia!")

    return bmi_result()

def main():
    Weight = float(input('Podaj wagę:'))
    High = float(input('Podaj wzrost (w metrach):'))

    res = bmi(Weight, High)
    print(res)
    your_BMI = bmi_result(res)
    print(your_BMI)


main()
