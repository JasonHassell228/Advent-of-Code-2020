f = open("input", "r")
current = {}
total = 0
for line in f.readlines():
    if line == "\n":
        print("curr:", current, "len:", len(current))
        total += len(current)
        current = {}
        print()
    for i in line.split():
        for j in i:
            current[j] = j
print("total:", total)
