f = open("input", "r")
input = []
for line in f.readlines():
    for i in line.split():
        input.append(int(line))

for i in input:
    for j in input:
        for k in input:
            if (i + j + k) == 2020:
                print(i * j * k)
                break
