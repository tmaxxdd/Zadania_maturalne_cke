#funkcja za kazdym razem zwracajaca liste z liczbami
def readCleanData():
  numbers = list()
  
  with open("liczby.txt") as data:
    #odczytaj linie
    numbers = data.readlines()
    #usuwa znaki pokroju '\n' oraz biale spacje
    numbers = [i.strip() for i in numbers]
    #rzutuje kazdy element z objektu string na obiekt int
    numbers = [int(x) for x in numbers]

  return numbers

#funkcja wypisująca mniejsze od 1000 oraz dwie ostatnie
def smallerThan1000():
  #wczytuje liczby do listy 'numbs'
  numbs=readCleanData()
  
  #odfiltrowywuje liczby mniejsze niz 1000 i zwraca do list 
  filtered=list(filter(lambda x: x < 1000, numbs))
  
  #z odfiltrowanych wyciaga 2 ostatnie pozycje
  lastTwo = filtered[:-3:-1]

  print("Mniejsze niż 1000: " + str(filtered))
  print("Ostatnie dwie: " + str(lastTwo))

#funkcja wypisujaca dzielniki liczb
def findDividersOf(number):
  dividers = list()
  for val in range(1, number + 1):
    if number % val == 0:
      dividers.append(val)

  #sortuje według wartości liczby 
  sorted(dividers, key=int)
  return dividers

#funkcja wypisujaca liczby z 18 dzielnikami
def find18Dividers():
  numbs = readCleanData()
  #deklaracja slownika na otrzymane wartości
  numbsWith18 = {}
  #iteracja po liczbach
  for numb in numbs:
    #znajdywanie dzielnikow
    if len(findDividersOf(numb)) == 18:
      
      #kod wykonuje sie dlugo, warto zaznaczyc, ze pracuje
      print("licze...")
      
      #w slowniku liczba jest kluczem a wartoscia lista z dzielnikami
      numbsWith18[numb] = findDividersOf(numb)

  print("Liczb z 18 dzielnikami jest: " + str(len(numbsWith18)))
  print("Liczby oraz ich dzielniki: " + str(numbsWith18))
  
#funkcja wypisujaca wzglednie pierwsza
def findMostPrimary():
  numbs = readCleanData()
  
  #odfiltrowywuje liczby niepodzielne przez 2
  notDividedBy2 = list(filter(lambda num: num % 2 != 0, numbs))
  
  #z notDividedBy2 odfiltrowywuje liczby niepodzielne przez 3
  notDividedBy3 = list(filter(lambda num: num % 3 != 0, notDividedBy2))
  
  #na koncu wyszukuje jakiekolwiek liczby zlozone
  
  #deklaracja listy liczb pierwszych
  primaryNumbers = list()
  #ilosc dzielnikow
  dividers = 0
  #iteracja po pozostalych liczbach
  for i in range(0, len(notDividedBy3)):
    #dla kazdej liczby
    for a in range(10, 101):
        # sprawdza dzielniki od 10 do 100
        if notDividedBy3[i] % a == 0:
          #zwieksz liczbe dzielnikow
          dividers = dividers + 1
          break
    
    #dodaje do listy tylko te liczby z dzielnikami 1 i siebie sama
    if dividers == 0:
      primaryNumbers.append(notDividedBy3[i])
      dividers = 0
      
  #wypisuje maksymalna wartosc
  print("Najwieksza wzglednie pierwsza: " + str(max(primaryNumbers)))

smallerThan1000()
find18Dividers()
findMostPrimary()
