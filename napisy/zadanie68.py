anagrams = [] #from excercise

with open("dane_napisy.txt") as data:
  for line in data:
    line = line.strip()
    pair = line.split()
    anagrams.append(pair)

def zad1():
  counter = 0
  for pair in anagrams:
    #only if both have same length
    if len(pair[0]) == len(pair[1]):
      #compare every letter
      if pair[0][::] == pair[1][::]:
        counter += 1

  return counter

def zad2():
  newAnagrams = [] #for sure anagrams
  counter = 0

  for pair in anagrams:
      first = pair[0]
      second = pair[1]
    
      if isAnagram(first, second): #anagrams
        newAnagrams.append([first, second])
        counter += 1

  return counter

def isAnagram(word1, word2):
  #only if both have same length
  if len(word1) == len(word2):
      a = set(word1[::])
      b = set(word2[::])
      if a == b:
        return True
  return False

example = [["BBBAAB", "BBBABA"], ["AAAA", "AAAAA"], ["AHHAH", "AHHAH"], ["BBABBABB", "BBBABB"], ["BABABB", "CACACC"]]

def zad3():
  k = 0
  allWords = [] 

  #replace pairs into singles ['BGA', 'CJI', ...]
  for pair in anagrams:
    allWords.append(pair[0])
    allWords.append(pair[1])

  for currentWord in allWords:
    # takes one word for example 'BBBAAB'
    counter = 0
    for word in allWords:
      #compare 'BBBAAB' with all words in file
      if isAnagram(currentWord, word):
        counter += 1

    if counter > k:
      k = counter

  return k

print("Wyrazy jednolite: " + str(zad1()))
print("Anagramy: " + str(zad2()))
print("Liczba k: " + str(zad3()))

