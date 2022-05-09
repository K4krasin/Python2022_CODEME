W = float(input('Podaj wagę:'))
H = float(input('Podaj wzrost (w metrach):'))


BMI = W/(H ** 2)
BMI = round(BMI, 2)

print()
print("Your BMI is:", BMI)
print("your BMI is:", round(W/(H ** 2), 3))