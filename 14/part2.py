
filename = "input.txt"

grid = set()

abyss = 0


with open(filename, "r") as file:
    lines = [[coord.split(",") for coord in line.split(" -> ")] for line in file.read().splitlines()]
    lines = [[(int(coord[0]), int(coord[1])) for coord in line] for line in lines]
    for line in lines:
        for (x1, y1), (x2, y2) in zip(line, line[1:]):
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid.add(x + y * 1j)
                    abyss = max(abyss, y + 1)


left = -1
right = 1
down = 1j

origin = 500 
sand = 0
while origin not in grid:
    pos = origin
    while True:
        if pos.imag < abyss:
            if pos + down not in grid:
                pos += down
                continue
            
            if pos + down + left not in grid:
                pos += down + left
                continue
            if pos + down + right not in grid:
                pos += down + right
                continue

        grid.add(pos)
        sand += 1
        break

print(sand)

