def loadCleanData(fileName):
  with open(fileName) as data:
    content = data.readlines()
    content = [x.strip() for x in content]
    #dane sa wciaz typu str
    values = [y.split(' ') for y in content[1::2]]
    
    index = 0
    for table in values:
      #konwersja ze str na int
      values[index] = [int(n) for n in table]
      index += 1

  #zwraca [ [1,2,3], [17,22,27] ]
  return(values)
  
def findDifference(numbers):
  diff = list()
  for i in range(0, len(numbers)):
    dif = numbers[i+1] - numbers[i]
    if dif in diff:
      return dif
    else:
      diff.append(dif)
  
def isArthmetic(numbers):
  difference = findDifference(numbers)
  
  for idx, el in enumerate(numbers):
    if idx != len(numbers)-1:
      if numbers[idx+1] - el != difference:
        return False
  return True
  

  
def isPerfectCube(x):
  #podnosi liczbe do potegi 1/3 (pierwiastek z 3)
  root = x ** (1. / 3)
  #zaokragla liczbe do calosci
  root = round(root)
  #rzutuje na typ Int
  root = int(root)
  
  #ponownie podnosi liczbe do potegi i sprawdza 
  #czy jest taka sama jak wejściowa
  return root ** 3 == x
  
def arthProgression():
  #tablice jak [ [1,2,3], [17,22,27] ]
  tables = loadCleanData("ciagi.txt")
  arthStrings = list()
  differences = list()
  
  for numbers in tables:
    if isArthmetic(numbers):
      #jesli ciag jest artmetyczny
      arthStrings.append(numbers)#dodaj ciag
      differences.append(findDifference(numbers))#dodaj jego roznice
      
  print("Artmet. ciagow jest: " + str(len(arthStrings)))
  print("Najwieksz roznica wynosi: " + str(max(differences)))
  
def biggestCube():
  tables = loadCleanData("ciagi.txt")
  #zadeklarowana lista pod szesciany
  cubes = list()
  #iteruje po wierszach
  for line in tables:
    cubesInLine = list()
    #iteruje po liczbach w wierszu
    for number in line:
      #sprawdza czy liczba jest szescianem
      if isPerfectCube(number):
        cubesInLine.append(number)
    #jesli lista nie jest pusta, 
    #bierze maksymalna wartosc
    if cubesInLine:
      cubes.append(max(cubesInLine))
      
  print("Największe sześciany w ciągach to: " + str(cubes))
  
def wrongElements():
  lines = loadCleanData("bledne.txt")
  #deklaracja listy dla niepasujacych elementow
  wrongNumbers = list()
  
  for line in lines:
    difference = findDifference(line)
    #zmienna logiczna wskazujaca znalezienie elementu
    done = False

    for idx, number in enumerate(line):
      #petla wykonuje sie tylko jesli:
      #zaczyna od drugiego elementu
      #oraz nie zostal znalezieny element
      if idx != 0 and not done:
        previousItem = line[idx - 1]
        
        if number - difference != previousItem:
          wrongNumbers.append(number)
          #wskazujemy znalezienie
          done = True
          
  print("Bledne wyrazy to: " + str(wrongNumbers))
    
  
      
arthProgression()
biggestCube()
wrongElements()
    
