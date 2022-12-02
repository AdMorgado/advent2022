
filename = "./input.txt"

lists = []
with open(filename, "r") as file:
    lists = [[int(num) for num in list.split("\n")] for list in file.read().split("\n\n")];

sums = list(map(lambda list: sum(list), lists))
sortedSums = sorted(sums, reverse=True)

print(sortedSums[0] + sortedSums[1] + sortedSums[2])
