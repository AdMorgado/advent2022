
filename = "input.txt"

def getLetterPriority(letter):
    if letter.isupper():
        return ord(letter) - ord('A') + 27
    else:
        return ord(letter) - ord('a') + 1

def getPriority(rucksack):
    compartment = set()

    halfLen = len(rucksack) // 2
    for i in range(0, halfLen):
        compartment.add(rucksack[i]) 

    for i in range(halfLen, len(rucksack)):
        if(rucksack[i] in compartment):
            sharedItem = rucksack[i]
    
    return getLetterPriority(sharedItem)

lines = []
with open(filename, "r") as file:
    lines = file.read().splitlines()



priorities = list(map(getPriority, lines))
print(sum(priorities))
