
filename = "input.txt"

with open(filename, "r") as file:
    lines = [[[int(num) for num in pair.split("-")] for pair in line.split(",") ] for line in file.read().splitlines()]

overlaps = 0
for pair in lines:
    leftRange = range(pair[0][0], pair[0][1] + 1)
    rightRange = range(pair[1][0], pair[1][1] + 1)

    if pair[0][0] in rightRange and pair[0][1] in rightRange:
        overlaps += 1
    elif pair[1][0] in leftRange and pair[1][1] in leftRange:
        overlaps += 1

print(overlaps)

