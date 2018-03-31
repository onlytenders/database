file = open('database.txt', 'r')

least = [500, 0]

leastLine = []

for line in file:
    tovar = line.split(",")
    if int(tovar[4]) < int(least[0]):
        least[0] = int(tovar[4])
        least[1] += 1
        leastLine = tovar

print(leastLine[1])
print(leastLine[4])
