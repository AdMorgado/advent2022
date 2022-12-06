import queue

filename = "input.txt"

input = open(filename, "r").read()

idxs = {}

window_width = 4

start = 0

for i in range(len(input)):
    char = input[i]

    if char in idxs:
        lastIdx = idxs[char] + 1
        if lastIdx > start:
            start = lastIdx

    idxs[char] = i

    if i - start == window_width-1:
        print(i+1)
        break



