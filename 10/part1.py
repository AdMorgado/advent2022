import queue

filename = "input.txt"

with open(filename, "r") as file:
    commands = file.read().splitlines()

def getSignalStrength(cycle, registerValue): return cycle * registerValue

def getOperation(command):
    match command.split(" "):
        case ["noop"]:      return (1, 0)
        case ["addx", arg]: return (2, int(arg))
    

cycle = 1
register = 1
executing = None
signalStrengths = []
while commands or executing:
    # get signaç
    if cycle % 40 == 20 and cycle <= 220:
        signalStrength = getSignalStrength(cycle, register)
        signalStrengths.append(signalStrength)
    
    # Execution
    if not executing:
        cmd = commands.pop(0)
        executing = getOperation(cmd)
    cycle += 1
    executing = (executing[0] - 1, executing[1])
    if executing[0] == 0:
        register += executing[1]
        executing = None

print(sum(signalStrengths))
