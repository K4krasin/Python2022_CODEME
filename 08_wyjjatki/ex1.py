#  Stwórz listę składającą się z kilku elementów różnego typu np. [13, ‘string’, 2.45] itp.
#  W pętli spróbuj wykonać dzielenie 10 przez wartość z listy. Złap wyjątki jakie mogą się przy tej okazji wydarzyć.

def main():
    list = [2, 'Gandalf', 24.41, 'Opos', '4 Pory Roku', 100, 0, {}, [1, 4]]

    for i in list:
        try:
            result = 10/list[i]
            print(result)
        except TypeError as err:
            print(f'No bląd {list[i]}', err)


main()
