
filename = "./input.txt"

lists = []
with open(filename, "r") as file:
    lists = [[int(num) for num in list.split("\n")] for list in file.read().split("\n\n")];

sums = map(lambda list: sum(list), lists)
maxSum = max(sums)
print(maxSum)
