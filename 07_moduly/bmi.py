def get_weight_high():
    Weight = float(input('Podaj wagę:'))
    High = float(input('Podaj wzrost (w metrach):'))

    return Weight, High

def bmi(waga, wzrost):
    return round(waga/wzrost ** 2,2)

def bmi_result(bmi_res):
    if bmi_res < 18.50:
        return ("Niedowaga!")

    elif bmi_res < 25:
        return ("Pożądana masa ciała!")

    elif bmi_res < 30:
        return ("Nadwaga!")

    else:
        return ("Otyłość!")


    return bmi_result()



def main():
    dane = get_weight_high()
    res = bmi(dane[0], dane[1])
    print(res)
    your_BMI = bmi_result(res)
    print(your_BMI)

if __name__ == '__main__':

    main()
