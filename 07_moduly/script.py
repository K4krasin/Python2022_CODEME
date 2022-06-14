import ex5

def main():
    total = 0
    next_pol = True
    while next_pol == True:
        fog = ex5.check_figure()
        pol = ex5.select_method(fog)
        print(pol)
        total = total + pol
        print("Czy chcesz dodać kolejne pole?")
        con = input("Jesli chcesz dodać kolejną figurę: napisz 'T'. W przeciwnym razie napisz dowolną literę: ")
        con = con.upper()
        if con == 'T':
            next_pol == True
        else:
            next_pol == False
            break

    print("Całkowita powierzchnia wynosi:", round(total, 2))

main()
