print(23+3==15+12)
print(29//7==5)
print(27%8==3)
num = 1234
print(f'czy liczba {num} jest parzysta:', num % 2 == 0)


#STRING
txt = "Pozdrawiam z podkarpacia"
print(txt[::])
print(txt[::-1])
print(txt[5:13:2])
print(txt[:11:1] + txt[12:])

txt2 = "Mata"
print(txt2.replace("M", "T"))
print(txt2)
txt3 = "412432532a"
print(str.isnumeric(txt3))
print()
new_txt = txt.center(50, '^')
print(new_txt)
print()
print(str.isupper(txt))

cutt = txt.rstrip('a')
print(cutt)

txt4 = "banana"
print(txt4.count("na"))

#Zadania


word = "dlugieslowo"
lengh = len(word)
cen = lengh//2
prev = cen - 1
next = cen + 1
print(cen, word[prev] + word[cen] + word[next])

text = "Honesty is the first chapter in the book of wisdom."

print(len(text))
print(text[-7:-1:1])
half = len(text)//2
print(text[:half])
print(text[-1])
print(text[:half:3])
print(text[::2])
print(text[::-1])
print(text.replace("wisdom", "frindship"))




