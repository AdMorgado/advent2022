
import numpy as np

filename = "input.txt"

with open(filename, "r") as file:
    input = list(map(lambda elem: [int(num) for num in elem.split(",")], file.read().splitlines()))
    positions = [(pos[2], pos[1], pos[0]) for pos in input]


def getFaces(pos):
    faces = set()
    z, y, x = pos
    # x faces
    faces.add((2, (z, y, x)))
    faces.add((2, (z, y, x+1)))
    # y faces
    faces.add((1, (z, y, x)))
    faces.add((1, (z, y+1, x)))
    # z faces
    faces.add((0, (z, y, x)))
    faces.add((0, (z+1, y, x)))
    return faces

blocks = set()
faces = dict()

i = 0
for pos in positions:
    i += 1
    if i % 10 == 0: print(i)
    blocks.add(pos)
    blockFaces = getFaces(pos)
    for face in blockFaces:
        if face in faces.keys():
            faces[face] += 1
        else:
            faces[face] = 1


faces = {face: count for face, count in faces.items() if count == 1}

print(len(faces))
