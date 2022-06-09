import random


def get_five_quoutes():
    with open('cytat.txt', encoding='utf-8') as fopen:
        quotes = fopen.readlines()
        firstfive = quotes[0:5]
    return quotes


def three_random():
    with open('cytat.txt', encoding="utf-8") as fopen:
        content = fopen.readlines()
    qoute = []
    i = 0
    while i != 3:
        qoute = qoute.append(random.choice(content))
        content = content.remove(qoute)
        i += 1
    return qoute

def main():
    five_q = get_five_quoutes()
    #print(five_q[3])
    #for i in five_q:
    #    print(i)
    with open('cytat.txt', encoding="utf-8") as fopen:
        content = fopen.readlines()
    qoute = []

    for i in range(0,3):
        X = random.choice(content)
        qoute.append(X)
        content.remove(X)
    for i in qoute:
        print(i)

main()



