
filename = "input.txt"

monkey = {}
for line in open(filename):
    name, order = line.strip().split(": ")

    args = order.split(" ")
    if len(args) == 1:
        order = int(args[0])
    else:
        lhs = args[0]
        rhs = args[2]
        if len(args[0]) != 4: lhs = int(lhs)
        if len(args[2]) != 4: rhs = int(rhs)
        order = (lhs, rhs, args[1])
    monkey[name] = order

print(monkey["root"])

def eval_order(order, monkey):
    if isinstance(order, int):
        return order
    lhs = eval_order(monkey[order[0]], monkey)
    rhs = eval_order(monkey[order[1]], monkey)
    if order[2] == "+":
        return lhs + rhs
    elif order[2] == "-":
        return lhs - rhs
    elif order[2] == "*":
        return lhs * rhs
    elif order[2] == "/":
        return lhs // rhs

print(eval_order(monkey["root"], monkey))


