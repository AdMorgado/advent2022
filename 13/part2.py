
from ast import literal_eval
from functools import cmp_to_key

filename = "input.txt"

packets = []
with open(filename, "r") as file:
    pairs = [[literal_eval(line) for line in pair.split("\n")] for pair in file.read().split("\n\n")]
    for pair in pairs:
        packets = packets + [pair[0], pair[1]]

dividerPackets = [ [[2]], [[6]] ]
packets += dividerPackets

class Ternary:
    FALSE = -1
    TRUE = 1
    UNKNOWN = 0

def process(left, right):
    leftType = type(left)
    rightType = type(right)

    if leftType == rightType:
        if leftType is int:
            diff = left - right
            if left == right:
                return Ternary.UNKNOWN
            elif left < right:
                return Ternary.TRUE
            else: 
                return Ternary.FALSE
        if leftType is list:
            size = min(len(left), len(right))
            for i in range(size):
                res = process(left[i], right[i])
                if res is Ternary.FALSE:
                    return Ternary.FALSE
                elif res is Ternary.TRUE:
                    return Ternary.TRUE
            if len(left) < len(right):
                return Ternary.TRUE
            if len(left) > len(right):
                return Ternary.FALSE

            return Ternary.UNKNOWN 

    elif leftType is int:
        return process([left], right)
    elif leftType is list:
        return process(left, [right])

packets = reversed(sorted(packets, key=cmp_to_key(process)))

dividerIndexes = 1
for i, packet in enumerate(packets):
    if packet in dividerPackets:
        dividerIndexes *= i + 1

print(dividerIndexes)

