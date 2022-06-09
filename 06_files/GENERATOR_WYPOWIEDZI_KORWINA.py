def first_part():
    with open('Pierwsza_czesc.txt', encoding="utf=8") as f:
        current_line = f.readlines()

    return current_line




def main():
    pierw = first_part()
    print(pierw)

main()