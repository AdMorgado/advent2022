
filename = "input.txt"

stacks = []
moves = []

def getElements(line):
    return [line[i] for i in range(1, len(line)-1, 4)]

def makeIntoMove(line):
    proto = line.split(" ")
    return [int(proto[1]), int(proto[3]), int(proto[5])]

with open(filename, "r") as file:
    stackInput, moveInput = file.read().split("\n\n")
    elems = list(map(getElements, stackInput.split("\n")[:-1]))
    stackWidth = len(elems[0])
    stacks = [[] for i in range(stackWidth)]
    for y in range(len(elems)-1, -1, -1):
        for x in range(stackWidth):
            elem = elems[y][x]
            if elem != " ": stacks[x].append(elem)

    moves = list(map(makeIntoMove, moveInput.splitlines()))

def makeMove(stacks, move):
    sorcIdx = move[1]-1
    destIdx = move[2]-1

    removed = stacks[sorcIdx][-move[0]:]
    stacks[sorcIdx] = stacks[sorcIdx][:-move[0]] 

    stacks[destIdx] += reversed(removed)

for move in moves:
    makeMove(stacks, move)

result = [stack.pop() for stack in stacks]
print("".join(result))

