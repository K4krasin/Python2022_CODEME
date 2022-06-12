def fibbonaci():
    n = int(input("Podaj liczbę do ciąguFibbonaciego: "))
    n1 = 0
    fib = [n1, n]
    nx = n

    for i in range(0,15):
        nx = fib[-1] + fib[-2]
        fib.append(nx)

    return fib