# genotype starts with AA and ends with BB
def findGen(line):
  gens = []
  endingPostition = 0 #last end postition
  #go through all characters
  for i in range(0, len(line) - 1):
    #find start pattern
    if line[i] == "A" and line[i+1] == "A":
      # Found AA
      gen = ""
      #Ensure that end was found
      if i >= endingPostition: 
        k = i # select start index
        #go through chars (i -> end - 1)
        for k in range(i, len(line) - 1):
          #find end pattern
          if(line[k] == "B" and line[k+1] == "B"):
            # found ending
            endingPostition = k #define where should start
            gen += "BB"
            break
          else:
            # not found ending. Add next char
            gen += line[k]

      # won't add gen if not have ending
      if gen.find("BB") > 0:
        gens.append(gen)
      
      gen = ""

  return gens

#TEST
print("\nFinding gen test: ")
assert(findGen("AACDBABBBCDAABCBBAAE") == ["AACDBABB", "AABCBB"])
assert(findGen("AADBAADDDDEEEBB") == ["AADBAADDDDEEEBB"])
print("OK")

genotypes = []
allGenes = []
with open("dane_geny.txt") as data:
  for line in data:
    line = line.strip()
    genotypes.append(line)
    allGenes.append(findGen(line))

def zad1():
  species = set() #not repeat
  maxNumber = 0

  # add unique species
  for i in range(0, len(genotypes)):
    species.add(len(genotypes[i]))

  for spec in species:
    counter = 0
    for genot in genotypes:
      if len(genot) == spec:
        counter += 1

    if counter > maxNumber:
      maxNumber = counter

  print("Liczba gatunkow: " + str(len(species)))
  print("Najwiekszy gatunek: " + str(maxNumber))

def zad2():
  counter = 0
  #go through genes of an individual
  for genes in allGenes:
    # go through all genes
    for gen in genes:
      if gen.find("BCDDC") > -1:
        counter += 1
        break

  return counter

def zad3():
  maxLength = 0
  maxGenes = 0
  #go through genes of an individual
  for genes in allGenes:
    if len(genes) > maxGenes:
      maxGenes = len(genes)

  print("Najwiecej genow: " + str(maxGenes))

  for genes in allGenes:
    for gen in genes:
      if len(gen) > maxLength:
        maxLength = len(gen)
  
  print("Najdluzszy gen: " + str(maxLength))

def zad4():
  immune = 0
  veryImmune = 0

  #Go through all genotypes
  for i in range(0, len(genotypes)):
    #Take one genotype
    currentGenot = genotypes[i]
    counter = 0
    for gen in allGenes[i]:
      #find reversed gens in it
        if currentGenot.find(gen[::-1]) > -1:
          counter += 1

    if counter == len(allGenes[i]):
      immune += 1

  #OK
  for genot in genotypes:
    #palindrome algorithm
    if genot[::] == genot[::-1]:
      veryImmune += 1

  print("Gatunki odporne: " + str(immune))
  print("Gatunki bardzo odporne: " + str(veryImmune))

print("\nExcercise: ")
zad1()
print("Osobniki z mutacja: " + str(zad2()))
zad3()
zad4()
