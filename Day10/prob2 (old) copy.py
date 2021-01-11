# f = open("input", "r")
# f = open("test", "r")
# f = open("test2", "r")
f = open("test3", "r")

inp = []
curPaths = []
prevPaths = []
pathList = {}
numPaths = {} # Keeps track of number of ways to get to each number
paths = 1

for line in f.readlines():
    for i in line.split():
        inp.append(int(line))
inp.sort()
inp.append(inp[-1] + 3)
inp.append(0)
inp.sort()
print(inp)

for i in range(len(inp) - 1):
    cur = inp[i]
    nex = inp[i + 1]
    lim = cur + 3
    options = []
    for j in inp[i:]:
        if j <= lim:
            if j != inp[i]:
                options.append(j)
        else:
            break
    if len(options) > 1:
        current = inp[i]
        if not curPaths:
            curPaths = options
        else:
            prevPaths = curPaths
            curPaths = options
        # "prev", prevPaths, , "len", len(curPaths))
        # print("options for", current, "cur", curPaths)
        pathList[current] = options # pathList[n][0] = current, pathList[n][1] = options for current

print(pathList)
for i in pathList:
    for j in pathList.get(i):
        if numPaths.get(j):
            numPaths[j] += 1
        else:
            numPaths[j] = 1
print(numPaths)