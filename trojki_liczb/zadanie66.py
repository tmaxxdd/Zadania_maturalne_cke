trios = []

with open("trojki.txt") as data:
  for line in data:
    line = line.strip()
    trio = line.split(" ")
    trios.append(trio)

def zad1():
  for trio in trios: 
    numbers1 = [int(i) for i in trio[0]] # 12 -> [1, 2]
    numbers2 = [int(j) for j in trio[1]]

    if sum(numbers1) + sum(numbers2) == int(trio[2]): 
      print(trio)

def zad2():
  for trio in trios: #change with trios
    first = int(trio[0])
    second = int(trio[1])
    if isPrime(first) and isPrime(second):
      if first * second == int(trio[2]):
        print(trio)

def zad3():
  for i in range(0, len(trios) - 1): #change with trios
    if isSquareTriangle(trios[i]) and isSquareTriangle(trios[i+1]):
      print(trios[i])
      print(trios[i+1])
      print("")

def zad4():
  counter = 0
  sequences = []

  for i in range(0, len(trios)):
      if isTriangle(trios[i]):
        counter += 1
        sequences.append(1)
      else:
        sequences.append(0)

  print(counter)
  print(findLongestSequence(sequences))

# See more here -> https://stackoverflow.com/questions/40166522/find-longest-sequence-of-0s-in-the-integer-list
def findLongestSequence(values):
  count = 0
  prev = 0
  indexend = 1
  for i in range(0, len(values)):
      if values[i] == 1:
          count += 1
      else:            
        if count > prev:
          prev = count
          indexend = i
        count = 0

  return prev

def isPrime(num):
  if num>1:
    for i in range(2, num):
      if (num % i) == 0:
        return False
    else:
      return True

  else:
    return False

def isSquareTriangle(numbers):
  numbers = [int(i) for i in numbers]
  maxLen = max(numbers)
  numbers.remove(maxLen)

  minLen = min(numbers)
  numbers.remove(minLen)

  if pow(minLen, 2) + pow(numbers[0], 2) == pow(maxLen, 2):
    return True
  else:
    return False

def isTriangle(numbers):
  numbers = [int(i) for i in numbers]

  a = min(numbers)
  numbers.remove(a)

  c = max(numbers)
  numbers.remove(c)

  b = numbers[0]

  # https://en.wikipedia.org/wiki/Triangle_inequality
  return a < b+c and b < a+c and c < a+b

print("---zadanie 1---")
zad1()
print("---zadanie 2---")
zad2()
print("---zadanie 3---")
zad3()
print("---zadanie 4---")
zad4()
