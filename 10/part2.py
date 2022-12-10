import queue

filename = "input.txt"

with open(filename, "r") as file:
    commands = file.read().splitlines()

def getOperation(command):
    match command.split(" "):
        case ["noop"]:      return (1, 0)
        case ["addx", arg]: return (2, int(arg))
    
width = 40

cycle = 0
register = 1
executing = None

buffer = ""
while commands or executing:

    # Rendering
    cycleMod = cycle % width
    if abs(register - (cycleMod)) < 2:
        buffer += "#"
    else:
        buffer += "."

    if cycleMod == width - 1:
        buffer += "\n"

    # Execution
    if not executing:
        cmd = commands.pop(0)
        executing = getOperation(cmd)

    cycle += 1
    executing = (executing[0] - 1, executing[1])
    if executing[0] == 0:
        register += executing[1]
        executing = None

print(buffer)