
import numpy as np

filename = "input.txt"

start = ord("S") - ord('a')
goal = ord("E") - ord('a')

with open(filename, "r") as file:
    lines = file.read().splitlines()
    lines = [[ord(char) - ord('a') for char in line] for line in lines]
    heightmap = np.array(lines, dtype=np.int16)
    beginning = np.where(heightmap == start)

steps = 0

def getNeighbors(node, heightmap):
    y, x = node
    neighbors = []
    if x > 0:                       neighbors.append((y, x - 1))
    if y > 0:                       neighbors.append((y - 1, x))
    if x < heightmap.shape[1] - 1:  neighbors.append((y, x + 1))
    if y < heightmap.shape[0] - 1:  neighbors.append((y + 1, x))
    return neighbors

totalSteps = 0

queue = [beginning]

steps = np.zeros(heightmap.shape, dtype=np.int16)

while queue:
    position = queue.pop(0)
    nSteps = steps[position][0]
    level = heightmap[position][0]
    
    for neighbor in getNeighbors(position, heightmap):
        neighborLevel = heightmap[neighbor][0]
        if neighborLevel == goal and level >= ord('z') - ord('a') - 1:
            totalSteps = nSteps + 1
            queue.clear()
            break
        if level != start and neighborLevel > level + 1: 
            continue
        if steps[neighbor] != 0: 
            continue
        
        queue.append(neighbor)
        steps[neighbor] = nSteps + 1


print("-- STEPS --")
print(steps)
print("\nTotal Steps:", totalSteps)