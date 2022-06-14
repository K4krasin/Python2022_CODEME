# Stwórz program, który dla dowolnego ciągu znajduje najdłuższą sekwencję takich samych znaków oraz jej długość np.
#
# Wejście:
# var = ‘banannnnannnnnnnnnanananananaaaana’
#
# Wyjście
# ‘nnnnnnnnn’, 9
#
# Utwórz generator instancji testowych, który wygeneruje losowe ciągi znaków składające się z jedynie z cyfr od 0-9. Upewnij się, że conajmniej 2 takie same znaki znajdą się w sekwencji.
#
# Zmodyfikuj generator tak, by oczekiwał znaków podanych przez użytkownika np. użytkownik podaje 4 znaki: ‘a’, ‘b’, ‘c’, ‘*’.
#
# Zaimportuj generator bezpośrednio do programu.

import ex6_generator as gen

def find_letter(word):
    max = 0
    max_letter = word[0]
    for i in range(0,len(word)):
        let = word[i]
        check = word.count(let)
        if check > max:
            max = check
            max_letter = let
        else:
            continue


    return max, max_letter


def main():

    var = gen.random_numbers()
    max_letter, letter = find_letter(var)
    print(var)
    print(max_letter, letter*max_letter)

if __name__ == '__main__':
    main()