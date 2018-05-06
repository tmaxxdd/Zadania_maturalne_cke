def openFile(source):
  with open(source) as f:
    content = f.readlines()
    #usuniecie znakow specjalnych
    content = [x.strip() for x in content]
    return content
    
base8Numbers = openFile("liczby1.txt")
base10Numbers = openFile("liczby2.txt")
    
def getInBase(liczba, system):
  wynik = ""
  # kiedy liczba nie jest 0
  while liczba > 0:
    # dzielenie modulo przez system zeby dac reszte
    reszta = liczba % system
                  # konwertujemy na tekst
    wynik = wynik + str(reszta)
    # '/' dzielenie z przecinikiem
    # '//' dzielnie calkowite
    liczba = liczba // system
  # spisujemy liczby od konca (od dolu)
  wynik = wynik[::-1]
  return wynik

def findMinAndMax():
  #Find min
  mini = getInBase(int(min(base8Numbers)), 8)
  print("Min is: " + str(mini))
  
  #Find max
  maxi = getInBase(int(max(base8Numbers)), 8)
  print("Max is: " + str(maxi))

#znajduje rosnacy ciag
def findIncreasingString(dataList):
  #Needed 999 elements
  leng = len(dataList)
  longest = list()#najwiekszy ciag
  incr = list() #bufor niemalejacego ciagu
  
  #konwersja na typ int
  for i in range(leng):
    dataList[i] = int(dataList[i])
    
            #zabezpieczenie przed out of range
  for idx in range(leng - 1):
    #sprawdza nastepny wyraz
    if dataList[idx + 1] >= dataList[idx]:
      incr.append(dataList[idx])
    #nastepny wyraz jest niemalejacy
    else: 
      incr.append(dataList[idx])#dodaje ostatni rosnacy wyraz
      #porownuje dlugosci
      if len(incr) > len(longest):
        #jesli nowy jest wiekszy to nadpisuje
        longest = incr
      #czysci bufor
      incr = list()
  
  return longest
  
def theLongestString():
  stringsList = findIncreasingString(base10Numbers)
  print("Pierwszym elementem jest: " + str(stringsList[0]))
  print("Dlugosc wynosi: " + str(len(stringsList)))

def compareNumbers():
  theSame = 0
  bigger = 0
  numbs1 = list()#liczb1.txt (typ int)
  numbs2 = list()#liczb2.txt (typ int)
  
  #rzutuje str na int
  for k in range(1000):
    numbs1.append(int(base8Numbers[k]))
    numbs2.append(int(base10Numbers[k]))
  
  for i in range(1000):
    #konwersja na ta sama podstawe
    num1 = numbs1[i]
    num2 = int(getInBase(numbs2[i], 8))
    
    #sprawdzenie wartosci
    if num1 == num2:
      theSame = theSame + 1
      
    if num1 > num2:
      bigger = bigger + 1
      
  print("Takich samych jest: " + str(theSame))
  print("Wiekszych jest: " + str(bigger))
  
def findSix():
  howManyIn8 = 0
  howManyIn10 = 0
  
  for number in base10Numbers:
    
    #10base
    for letter10 in str(number):
      if letter10 == "6":
        howManyIn10 = howManyIn10 + 1
        
    #8base
    newNumb = getInBase(number, 8)
    for letter in newNumb:
      if letter == "6":
        howManyIn8 = howManyIn8 + 1
    
  print("W sys. dzies.: " + str(howManyIn10))
  print("Zapisane osemkowo: " + str(howManyIn8))
  

findMinAndMax()
theLongestString()
compareNumbers()
findSix()
