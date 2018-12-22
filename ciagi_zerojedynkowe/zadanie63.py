def loadCleanData(fileName):
  with open(fileName) as data:
    content = data.readlines() #list with whitechars (\n)
    content = [x.strip() for x in content]
  return content

series = loadCleanData("ciagi.txt")

def doubleCycle():
  counter = 0
  for serie in series:
    if (len(serie) % 2 == 0): # only the even series
      half = int(len(serie) / 2) # take a middle of string
      if serie[:half] == serie[half:]: # check if first half equals second half
        counter += 1

  return counter

def twinOnes():
  counter = 0
  #for all the numbers
  for serie in series:
    #for every letter in string (0 or 1)
    for i in range(0, len(serie)):
      if i < len(serie) - 1:
        if serie[i] == "1" and serie[i + 1] == "1":
            #There is "...11..."
            break
        else:
          #reaches the end of number
          if i == len(serie) - 2:
            counter += 1

  return counter

def semiPrimeNumbers():
  semiPrimes = []
  decValues = [int(x, 2) for x in series] #from bits to decimal
  for number in decValues: #do for every number
    if number > 1: #1 cannot be a semiprime
      if (hasPrimeDividers(number)):
          semiPrimes.append(number)

  print("min = " + str(min(semiPrimes)))
  print("max = " + str(max(semiPrimes)))

  return len(semiPrimes)

def hasPrimeDividers(number):
  #Primes start from 2
  for divider in range(2, number + 1): #do until divider equals number
    if (isPrime(divider)): #do only if one divider is prime
      if number % divider == 0:
        #check the second divider
        if (isPrime(number / divider)): #divided number must be also prime
          return True
        else:
          #second divider isn't prime
          return False
          break

  return False

# Suggested by user dawg on the stackoverflow
# https://stackoverflow.com/a/15285588
def isPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True 
  
print("Jest: " + str(doubleCycle()) + " ciagow dwucyklicznych")
print("Ilosc ciagow w ktorych nie wystepuja jedynki obok siebie: " + str(twinOnes()))
print("Jest " + str(semiPrimeNumbers()) + " liczb polpierwszych");
