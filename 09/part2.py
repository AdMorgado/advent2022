
filename = "input.txt"

with open(filename, "r") as file:
    motions = [line.split(" ") for line in file.read().splitlines()]
    motions = [(dir, int(val)) for dir, val in motions]


directions = {
    "U": ( 0,  1),
    "R": ( 1,  0),
    "D": ( 0, -1),
    "L": (-1,  0)
}

numOfKnots = 10
numOfTails = numOfKnots - 1
head = (0, 0)
tails = [(0, 0) for i in range(numOfTails)]


visited = set([(0, 0)])

def followHead(tail, head):

    diffX = head[0] - tail[0]
    diffY = head[1] - tail[1]

    #manhattan distance
    dist = abs(diffX) + abs(diffY)
    if dist <= 1 or (dist == 2 and abs(diffX) == abs(diffY)):
        return tail

    if diffX != 0 and diffY == 0:
        # horizontal move
        newX = tail[0] + (1 if head[0] > tail[0] else -1)
        return (newX, tail[1])
    elif diffX == 0 and diffY != 0:
        # vertical move
        newY = tail[1] + (1 if head[1] > tail[1] else -1)
        return (tail[0], newY)
    else:
        dirX = directions["L"] if diffX < 0 else directions["R"]
        dirY = directions["D"] if diffY < 0 else directions["U"]

        return (tail[0] + dirX[0], tail[1] + dirY[1]) 


for motion in motions:
    dir = directions[motion[0]]
    for i in range(motion[1]):
        head = (head[0] + dir[0], head[1] + dir[1])
        tails[0] = followHead(tails[0], head)
        for j in range(1, numOfTails):
            tails[j] = followHead(tails[j], tails[j-1])
        visited.add(tails[numOfTails-1])

print(len(visited))
