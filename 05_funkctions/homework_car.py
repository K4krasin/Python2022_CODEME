#  Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
#
# Program zacznie ze stworzonym słownikiem o trzech kluczach:
# marka (str)
#
# model (str)
#
# rocznik (int)
#
# Wypisze ten słownik na ekran (bez żadnego formatowania)
#
# Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
# “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
#
# Jeśli nie spełnia powyższego warunku, wypisze komunikat:
# “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
#
# Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!), aby zobaczyć, czy progam również zmienia swoje zachowanie.

car_dic = {
    'marka': 'Audi',
    'model': 'A3',
    'rocznik': 1993
}

print(car_dic)

def is_monument(car):
    if 2022 - car['rocznik'] > 24:
        print(f'Gratulacje! Twój samochód {car["marka"]} może być zarejestrowany jako zabytek.')
    else:
        print(f'Twój samochód {car["marka"]} jest jeszcze zbyt młody.')



# 9▹ Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej 75% oryginalnych części.
# W naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność w kategorii tak/nie.
#
# Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
# dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.
#
# ponownie wyświetl zmieniony słownik
#
# Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również od jego oryginalności. Dopisz odpowiednie komunikaty.

car_dic['czy_oryginalny'] = True

print(car_dic)

def is_original (auto):
    if auto['czy_oryginalny'] == True:
        print("Możesz go zarejestrować jako oryginalny")
    else:
        print("Twój samochód nie jest oryginalny w 75%")

is_monument(car_dic)
is_original(car_dic)