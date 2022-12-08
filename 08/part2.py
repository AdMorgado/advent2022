import numpy as np

filename = "input.txt"

input = [[int(char) for char in line] for line in open(filename, "r").read().split("\n")]
grid = np.array(input, dtype=np.int8)
score = np.ones(grid.shape, dtype=np.int32)

def checkRange(arr, idx, goRight):
    height = arr[idx]
    ran = range(idx + 1, arr.size)
    if not goRight: ran = range(idx - 1, -1, -1)

    length = 0
    for i in ran:
        length += 1
        if arr[i] >= height:
            break

    return length

for x in range(grid.shape[1]):
    sliced = grid[: , x]
    for y in range(grid.shape[0]):
        score[y, x] *= checkRange(sliced, y, True)
        score[y, x] *= checkRange(sliced, y, False)
        
for y in range(grid.shape[0]):
    sliced = grid[y, :]
    for x in range(grid.shape[1]):
        score[y, x] *= checkRange(sliced, x, True)
        score[y, x] *= checkRange(sliced, x, False)

print(score.max())