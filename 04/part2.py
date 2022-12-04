
filename = "input.txt"

with open(filename, "r") as file:
    lines = [[pair for pair in line.split(",") ] for line in file.read().splitlines()]


overlaps = 0
for pair in lines:
    a1, a2 = map(int, pair[0].split("-"))
    b1, b2 = map(int, pair[1].split("-"))

    if not((a1 <= b1 and a2 < b1) or (b1<=a1 and b2 < a1)):
        overlaps += 1 

print(overlaps)


