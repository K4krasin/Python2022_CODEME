import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)

def choice_gender(gender):
    if gender == 2:
        gender = 'Facet'
    elif gender == 1:
        gender = 'Kobieta'
    return gender

def select_role_by_age(age):
    if age < 16:
        return ("Twoja postać jest jeszcze niedojrzała na przygody. Cieszy się dzieciństwem i zbiera truskawki u babci na działce.")
    elif age < 25:
        age = 'Młodzieniec'
        return age
    elif age < 40:
        age = 'W sile wieku'
        return age
    elif age < 65:
        age = 'Doświadczony'
        return age
    else:
        return ("Jeszcze żyjesz? Ciesz się tą chwilą póki możesz i siedź w domu.")

    return select_role_by_age(age)

def intro_to_the_history(name, age, gender):
    if age == 'Młodzieniec' and (gender == 'Facet'):
        return (f'Znajdujesz się w środku pola na Twojej doskonale znanej wsi. Po szóstej godzinie pracy przysiadasz na chwilę pod pobliskiem drzewem. '
                f'Spoglądasz zw dal odległe góry i ich niezdobyte szczyty, wyobrażajać siebie na jednym z nich. To jest Twoje marzenie, móc kiedyś zajrzeć na swój ojczysty dom z drugiej perspektywy.'
                f'Z wysokości wyższej nawet niż lot ptaków. Jakie to musi być niesamowite uczucie. Z rozmyślenia wyrwał Cię spadający orzech, którego trajektoria lotu poprowadziła prosto na czubek Twojej głowy'
                f'Trzymając się za głowę wracasz do pracy. Marzenia są wspaniałe jednak pole, którym musisz się zajmować jest ważniejsze. Dzisiaj skazany jesteś tylko na siebie.'
                f'Twoi bracie pojechali do Vosburn - pobliskiego miasta na targ. Ich zadaniem było sprzedać część naszych zapasów na zimę za które można by było kupić lekarstwa dla ojca, który w ciężkim stanie lezy już od 3 dni w chacie na łóżku.'
                f'Trochę zazdrościsz im tego wyjazdu. Jednak jako najmłodszy i najmniej wygadany spośród wszystkich braci skazany byłeś na pozostanie i pracę w polu. Swoją drogą bracia powinni za niedługo wrócić z wyprawy.'
                f'Pochłonięty myślami w trakcie pracy nie usłyszałeś wołania.\n '
                f'- {name}! - To Twoja młodsza ledwie 10 letnia siostra przyszła po Ciebie - Chodź już. Matula Cię woła!\n'
                f'Faktycznie robił się zmierzch. Po zmierzchu z reguły było spokojnie jedynie sporadyczniepokazywały się zwykłe wilki. Jednak ostatnimi czasy także i im doskwierała bieda i głód i coraz odważniej wychodziły poza swojemiejsce żeru.'
                f'Po powrocie do chaty zmartwił Cię widok cierpiącego ojca. Zacząłeś się zastanawiać gdzie też podziewają się Twoi bracia. Również i matka wydawała się być zatroskana, chociaż nie wiesz czy bardziej odkąd ojciec zachorował.\n'
                f'- Widziałeś już nasz wóz gdzieś na horyzoncie? - Zapytała w końcu drżącym głosem. Zgodnie z prawdą kiwnąłeś przecząco głową. Przypomniałeś sobie jednak że w międzyczasie widziałeś wracającego na koniu sąsiada.\n'
                f'- Widziałem że młynarz Henryk wrócił już do siebie. - odpowiedziałem\n'
                f'- Może poszedłbyś zapytać czy przypadkiem nie spotkał po drodzę naszego wozu?')

    else:
        return ("resztę się kiedyś napisze xD")
    return intro_to_the_history()

def chapter1_of_histry(name, age, gender, history_young_man):
    if age == 'Młodzieniec' and (gender == 'Facet'):
        print(" 1) Pójdź do sąsiada.\n 2) Przeczekaj i uspokój mamę.")
        history_young_man = int(input("Twój wybór: "))
        if history_young_man == 1:
            print("Niewiele myśląc idziesz najkrótszą drogą do sąsiada. Dochodzisz do ogromnej chałupy. Znacznie większej od waszej. Chwytasz za kołatkę i rozlega się głośne pukanie. Dłuższą chwilę czekasz na odpowiedź jednak nic nie słychać")
            history_young_man = 'przezorny'
            return history_young_man
        elif history_young_man == 2:
            print("Próbujesz przemówić mamie, że wszystko jest w porządku i Twoi bracia jedynie musieli spotkać jakieś drobne kłopoty po drodzę. Przecież na drodzę do domu nie jest niebezpieczna i nigdy nie dochodzi tu do ataków gdyż jest zbyt ruchliwa na napady."
                  "W mieście też nie mogło się nic wydarzyć gdyż jest ono bardzo dokłądnie pilnowane przez straż. \n"
                  "siedzicie dłuższą chwilę w ciszy. Nagle pies za oknem zaczyna żarliwie szczekać, a z pobliskiej stodoły rozlega się ogromny huk. ")
            history_young_man = 'bojazliwy'
            return history_young_man
        else:
            print("Spada Ci garnek na łeb i przypominasz sobie że masz tylko 2 wybory")
            while history_young_man != 1 and (history_young_man != 2):
                print("Twój wybór: ")
                history_young_man = int(input())
        return chapter1_of_histry(name, age, gender, history_young_man)

def second_choise(history, name):
    if history == 'przezorny':
        print(" 1) Poczekaj jeszcze chwilę.\n 2) Porozglądaj się po podwórku sąsiada.\n 3) Wróć do domu")
        history = int(input('Twój wybór: '))
        if history == 1:
            print(f'Nic się tu chyba nie wydarzy. Próbujesz raz jeszcze i w momencie, w którym chcesz ostatni raz złapać za kołatkę uchylają się drzwi. Otwiera Ci Helena - żona Henryka. \n - Witaj {name}! '
                  f'Grzecznie się witasz. Helena zaprowadziła Cię do odpoczywającego młynarza. opowiadasz mu cel swojej wizyty i pytasz czy nie widział Twoich braci. Henryk zamysłił sie chwilę. \n'
                  f'- Widziałem ich dzisiaj parę razy. Jednak nawet nie miałem okazji z nimi porozmwawiać. Był za duży ruch. Ciężko mi powiedzieć kiedy widziałem ich ostatni raz. Jednak kiedy wyjeżdzałem to plac handlowy był niemal pusty i jestem prawie pewien że nie było ich już tam'
                  f'Gdy tylko skończył wypowiadać ostatnie słowo to z okolic Twojego domu było słychać ogromny huk.\n - Co to było? - szybko podszedłeś do okna próbując coś zauważyć jednak w pomieszzceniu w jakim sie znajdowałeś nie było żadnego okna wychodzącego na Twój dom.')
        elif history == 2:
            print("Kątem oka widzisz wóz, którym przyjechał Henryk z dzisiejszego jarmarku w Vosburn. Intuicja mówiCi że musisz tam podejść. ")
        elif history == 3:
            print("Wracasz powoli w stronę domu gdy nagle dostrzegasz ruch")
        else:
            print("Zrywa się wiatr. Wisząca nad drzwiami nieiwielka figurka mająca odstraszać złe duchy spada z gwoździa prosto na Twoją głowę. Przypominasz sobie, że masz tylko 3 wybory")
    elif history == 'bojazliwy':
        print(" 1) wybór \n 2) wybór")
        history = int(input('Twój wybór: '))
        if history == 1:
            print('cos')
        elif history == 2:
            print("XD")
        else:
            print("Dostajesz w łeb")
    return second_choise(history,name)

    return second_choise(history, name)



def main():
    print("Wybierz płeć: \n 1) Kobieta \n 2) Mężczyzna")
    hero = int(input())
    if hero != 1 and (hero != 2):
        while hero != 1 and (hero != 2):
            print("Wybierz płeć: \n 1) Kobieta \n 2) Mężczyzna")
            hero = int(input())
    hero_sex = choice_gender(hero)
    your_age = int(input("Podaj wiek swojego bohatera: "))
    hero_age = select_role_by_age(your_age)
    hero_name = input("Podaj imie jakim będą na Ciebie wołać!: ")
    hero_history = 0
    print(intro_to_the_history(hero_name, hero_age, hero_sex))
    hero_history = chapter1_of_histry(hero_name, hero_age, hero_sex, hero_history)
    second_choise(hero_history, hero_name)







main()
