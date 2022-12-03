
filename = "input.txt"

def getLetterPriority(letter):
    if letter.isupper():
        return ord(letter) - ord('A') + 27
    else:
        return ord(letter) - ord('a') + 1

def getOcurrence(rucksack): 
    ocurrence = set()

    for item in rucksack:
        ocurrence.add(item)
    
    return ocurrence


def getBadge(group): 

    sack1 = getOcurrence(group[0])
    sack2 = getOcurrence(group[1])

    return next(item for item in group[2] if item in sack1 and item in sack2) 

rucksacks = []
with open(filename, "r") as file:
    rucksacks = file.read().splitlines()

groups = [[rucksacks[i], rucksacks[i+1], rucksacks[i+2]]for i in range(0, len(rucksacks), 3)]


badges = list(map(getBadge, groups))
priorities = list(map(getLetterPriority, badges))
print(sum(list(priorities)))
