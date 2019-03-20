ulamki = [] #[ [licznik, mianownik], ... ]

#wprowadzanie dancych do tablicy
with open("dane_ulamki.txt") as dane:
    for wiersz in dane:
        wiersz = wiersz.strip()
        liczby = wiersz.split() # licznik mianownik
        liczby = [int(x) for x in liczby] #rzut. na int
        ulamki.append(liczby)

def zad1():
    #pobieramy wartosci pierwszego ulamka jako poczatkowe
    min_wart = float(ulamki[0][0]) / ulamki[0][1]
    min_licz = float(ulamki[0][0])
    min_mian = float(ulamki[0][1])

    for licznik, mianownik in ulamki:
        wartosc = float(licznik) / mianownik

        if wartosc <= min_wart:
            if wartosc == min_wart:
                if mianownik < min_mian:
                    min_mian = mianownik
                    min_licz = licznik
            else:
                min_wart = wartosc
                min_licz = licznik
                min_mian = mianownik

    return min_licz, min_mian

def zad2():
    ilosc = 0
    for licznik, mianownik in ulamki:
        if nwd(licznik, mianownik) == 1:
            ilosc += 1
    return ilosc

def zad3():
    suma = 0
    for licznik, mianownik in ulamki:
        licznik = licznik / nwd(licznik, mianownik)
        suma += licznik
    return suma

def zad4():
    licz = 0
    b = 4 * 9 * 25 * 49 * 13
    for licznik, mianownik in ulamki:
        licz = licz + b * licznik / mianownik
    return licz

def nwd(a, b):
    while b!=0:
        a, b = b, a % b

    return a
    
print(zad1())
print(str(zad2()))
print(str(zad3()))
print(str(zad4()))
