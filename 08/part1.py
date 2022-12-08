
import numpy as np

filename = "input.txt"

input = [[int(char) for char in line] for line in open(filename, "r").read().split("\n")]
grid = np.matrix(input, dtype=np.int8)
isVisible = np.zeros(grid.shape, dtype=bool)

xMax = grid.shape[1]-1
yMax = grid.shape[0]-1

for x in range(grid.shape[1]):
    highest = -1
    for y in range(grid.shape[0]):
        cell = grid[y, x]
        if cell > highest:
            isVisible[y, x] = True
            highest = cell

    highest = -1
    for y in range(yMax, -1, -1):
        cell = grid[y, x]
        if cell > highest:
            isVisible[y, x] = True
            highest = cell

        
for y in range(grid.shape[0]):
    highest = -1
    for x in range(grid.shape[1]):
        cell = grid[y, x]
        if cell > highest:
            isVisible[y, x] = True
            highest = cell

    highest = -1
    for x in range(xMax, -1, -1):
        cell = grid[y, x]
        if cell > highest:
            isVisible[y, x] = True
            highest = cell
        


print(isVisible.astype(np.int8))
print(isVisible.sum())