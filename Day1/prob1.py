f = open("input", "r")
input = []
for line in f.readlines():
    for i in line.split():
        input.append(int(line))

for i in input:
    for j in input:
        if (i + j) == 2020:
            print(i * j)
            break
