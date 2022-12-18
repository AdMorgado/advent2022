
import re

filename = "input.txt"
target = 2000000

# manhattan distance with a complex number
def manhanttanDistance(coords):
    return abs(coords.real) + abs(coords.imag)

with open(filename, "r") as file:
    lines = [list(map(int, re.findall("-?[0-9]+", line))) for line in file.read().splitlines()]
    lines = [(sensor[0] + sensor[1]*1j, sensor[2] + sensor[3]*1j)for sensor in lines]
    lines = [(sensor, beacon, manhanttanDistance(sensor - beacon)) for sensor, beacon in lines]

ranges = []


# create ranges for each sensor at a certain y value
for sensor, beacon, dist in lines:
    yDist = abs(sensor.imag - target)
    if yDist > dist: continue
    
    start = sensor.real - dist + yDist
    end = sensor.real + dist - yDist + 1
    fieldRange = range(int(start), int(end))
    #print(sensor, dist, fieldRange)
    ranges.append(fieldRange)

#for fieldRange in ranges:
    #print(fieldRange)


minX = min([fieldRange.start for fieldRange in ranges]) - 1
maxX = max([fieldRange.stop for fieldRange in ranges]) + 1


print("minX", minX)
print("maxX", maxX)
print("dist", maxX - minX)

beacons = set([beacon for sensor, beacon, dist in lines])

blocked = 0
for i in range(int(minX) - 1, int(maxX) + 1):
    pos = i + target * 1j
    if(i % 100000 == 0): print(i)
    if pos not in beacons and any([i in fieldRange for fieldRange in ranges]):
        blocked += 1

print(blocked)

