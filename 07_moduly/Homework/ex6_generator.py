import random

def random_numbers():
    num = ['0','1','2','3','4','5','6','7','8','9']

    for i in range(0,4):
        choice = input("Podaj losowy znak: ")
        num.append(choice)

    numbers = random.choices(num, k=9)

    return numbers
