import random
import os

def get_wuoute(file):
  with open(f'{file}.txt', encoding="utf-8") as fopen:
    content = fopen.readlines()

  quoute = random.choice(content)
  return quoute

def show(qoute):

  qoute = qoute.strip('\n')
  qoute = qoute.split(' - ')
  lenth = len(qoute[0]) + 20
  print('\nQoute of the day is:\n')
  print('*' * lenth)
  print(qoute[0].center(lenth))
  print(f'~{qoute[1]}~'.center(lenth))
  print('*' * lenth)




def main():

  name = input("Podaj nazwę pliku: ")
  quoute = get_wuoute(name)
  show(quoute)
  print(os.listdir())
  print(os.path.getsize('cytat.txt'))


main()