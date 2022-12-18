
import numpy as np

filename = "input.txt"

with open(filename, "r") as file:
    input = list(map(lambda elem: [int(num) for num in elem.split(",")], file.read().splitlines()))
    positions = [(pos[2] + 1, pos[1] + 1, pos[0] + 1) for pos in input]

Xs = [pos[2] for pos in positions]
Ys = [pos[1] for pos in positions]
Zs = [pos[0] for pos in positions]

maxX = max(Xs) + 2
maxY = max(Ys) + 2
maxZ = max(Zs) + 2



# returns the face that two blocks are touching
def getFaceBetweenTwoPoints(pointA, pointB):
    zA, yA, xA = pointA
    zB, yB, xB = pointB
    if zA == zB:
        if yA == yB:
            x = max(xA, xB)
            return (0, zA, yA, x)
        elif xA == xB:
            y = max(yA, yB)
            return (1, zA, y, xA)
    elif yA == yB and xA == xB:
        z = max(zA, zB)
        return (2, z, yA, xA)
        

# returns the neighbors as long as they are within the bounds
def getNeighbours(pos, maxX, maxY, maxZ):
    z, y, x = pos
    neighbors = []
    if x > 0:       neighbors.append((z, y, x-1))
    if y > 0:       neighbors.append((z, y-1, x))
    if z > 0:       neighbors.append((z-1, y, x))
    if x < maxX-1:  neighbors.append((z, y, x+1))
    if y < maxY-1:  neighbors.append((z, y+1, x))
    if z < maxZ-1:  neighbors.append((z+1, y, x))
    return neighbors
    

occupancy = np.zeros((maxZ, maxY, maxX), dtype=bool)

for pos in positions:
    occupancy[pos] = True

faces = set()

# get min and max of each axis faces
# Do 3d flood fill starting from 0,0,0 until it finds a block
queue = [(0, 0, 0)]
visited = set()
while queue:
    pos = queue.pop(0)
    if pos in visited: continue
    visited.add(pos)
    for neighbor in getNeighbours(pos, maxX, maxY, maxZ):
        if occupancy[neighbor] == True:
            faces.add(getFaceBetweenTwoPoints(pos, neighbor))
        else:
            queue.append(neighbor)

print(len(faces))

