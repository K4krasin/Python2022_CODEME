# Sprawdź jak wygląda kod modułu antigravity. Korzystając z tego samego sposobu otwarcia dowolnego url pozwól użytkownikowi podać adres www.
#
# Pamiętaj sprawdzić czy url jest prawidłowy może zaczynać się:
#
# https://
# http://
# www
# bez www
#
# Może się kończyć za pomocą:
#
# .pl
# .com
#
# Jeśli podany adres nie jest linkiem, podnieś wyjątek URLError, który będzie informował, że url jest nieprawidłowy.

import webbrowser

class URLError(Exception):
    '''custom error from url'''
    pass

def main():

    url = input('Podaj adres www: ')


    if url[0:4] == 'http' or (url[0:3] == 'www' or (url[0:5] == 'https') and (ulr[-1:-2] == 'pl' or (url[-1:-3] == com))):
        webbrowser.open(url)
    else:
        raise URLError('Niepoprawny start/koniec linku')




main()