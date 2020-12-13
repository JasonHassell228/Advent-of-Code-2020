f = open("input", "r")
# f = open("test", "r")

current = {}
toPop = {}
total = 0
for line in f.readlines():
    if line == "\n":
        for i in toPop:
            if current.get(i):
                current.pop(i)
        # print("current after:", current)


        # print("curr:", current, "len:", len(current))
        total += len(current)
        current = {}
        toPop = {}
        # print()
    if not current:
        for i in line.split():
            for j in i:
                current[j] = j
    else:
        # print("line", line[:-1])
        for i in line[:-1]:
            if i not in current:
                toPop[i] = i
                # print("current", current, "char", i)
        for i in current:
            if i not in line[:-1]:
                toPop[i] = i
        # print("topop:", toPop, "curr", current)


# print("topop:", toPop, "curr", current, "total", total)

if current and toPop:
    for i in toPop:
        if current.get(i):
            current.pop(i)
    # print("current after:", current)


# print("curr:", current, "len:", len(current))
total += len(current)
current = {}
toPop = {}
# print()

# print("current", current)
print("total:", total)
