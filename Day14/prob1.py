f = open("input", "r")
inp = []
for line in f.readlines():
    for i in line.split():
        inp.append(int(line))
print(inp)