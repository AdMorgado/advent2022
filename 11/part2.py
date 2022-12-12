
filename = "input.txt"

def makeMonkey(items, operation, div, testPass, testFail):
    return {
        "items": items,
        "operation": operation,
        "div": div,
        "testPass": testPass,
        "testFail": testFail,
        "count" : 0,
    }


monkeys = []
# So this is the true power of python... 
# not allowing to pass variables by value in lambdas. rethinking of switching langs.
pythonIsAGarbageLanguage = [] 

with open(filename, "r") as file:
    monkeyInput = file.read().split("\n\n")
    for monkey in monkeyInput:
        lines = monkey.split("\n")

        items = lines[1].replace("  Starting items: ", "").split(", ")
        items = list(map(int, items))

        operationSplit = lines[2].replace("  Operation: new = old ", "").split(" ")
        if(operationSplit[1] != "old"):
            opNumber = int(operationSplit[1])
            pythonIsAGarbageLanguage.append(opNumber)
            if operationSplit[0] == "*":
                operation = lambda x, i: x * pythonIsAGarbageLanguage[i]
            elif operationSplit[0] == "+":
                operation = lambda x, i: x + pythonIsAGarbageLanguage[i]
        else:
            pythonIsAGarbageLanguage.append("Trash")
            if operationSplit[0] == "*":
                operation = lambda x, i: x * x
            elif operationSplit[0] == "+":
                operation = lambda x, i: x + x

        test = int(lines[3].replace("  Test: divisible by ", ""))

        testPass = int(lines[4].replace("    If true: throw to monkey ", ""))
        testFail = int(lines[5].replace("    If false: throw to monkey ", ""))
        
        monkeys.append(makeMonkey(items, operation, test, testPass, testFail))

rounds = 10000

leastCommonMultiple = 1
for monkey in monkeys: leastCommonMultiple *= monkey["div"]

for j in range(rounds):
    #for monkey in monkeys:
    print(j)
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        while monkey["items"]:
            worry = monkey["items"].pop(0)
            worry = monkey["operation"](worry, i)
            monkey["count"] += 1
            #worry = worry // 3
            worry %= leastCommonMultiple
            if worry % monkey["div"] == 0:
                monkeys[monkey["testPass"]]["items"].append(worry)
            else:
                monkeys[monkey["testFail"]]["items"].append(worry)

monkeyBusiness = 0

topTwo = sorted([monkey["count"] for monkey in monkeys], reverse=True)[:2]
print("Top Two:", topTwo)
print("Monkey Business: ", topTwo[0] * topTwo[1])

