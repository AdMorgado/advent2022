
filename = "input.txt"

def getLetterPriority(letter):
    if letter.isupper():
        return ord(letter) - ord('A') + 27
    else:
        return ord(letter) - ord('a') + 1

def getPriority(rucksack):

    halfLen = len(rucksack) // 2
    firstCompartment = set(rucksack[slice(0, halfLen)])
    
    for i in range(halfLen, len(rucksack)):
        if(rucksack[i] in firstCompartment):
            sharedItem = rucksack[i]
    
    return getLetterPriority(sharedItem)

lines = []
with open(filename, "r") as file:
    lines = file.read().splitlines()



priorities = list(map(getPriority, lines))
print(sum(priorities))
