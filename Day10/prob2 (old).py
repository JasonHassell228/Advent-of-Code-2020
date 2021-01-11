# f = open("input", "r")
# f = open("test", "r")
# f = open("test2", "r")
f = open("test3", "r")

inp = []
curPaths = []
prevPaths = []
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
        count = 0
        print("paths:", paths, "prev", prevPaths, "cur", curPaths, "len", len(curPaths))
        if not prevPaths:
            paths *= len(curPaths)
        else:
            if current in prevPaths:
                # for k in prevPaths:
                #     if current >= k:
                #         count += 1
                # print(count, '*', len(options), '- 1', '=', count * len(options) - 1)
                # paths += len(curPaths) * count - 1

                paths += len(curPaths) - 1

                # for k in prevPaths:
                #     for m in curPaths:
                #         if m > k and m < (k + 4):
                #             # option from curPath is within range 1-3 of option from prevPath
                #             count += 1
                # paths += count
                
                
                # toAdd = 0
                # print(prevPaths, curPaths)
                # for l in prevPaths:
                #     if l in curPaths:
                #         toAdd += 1
                # paths += toAdd - 1
            else:
                paths *= len(curPaths)

            print("prev", prevPaths, "cur", curPaths, "current", current, "len", len(curPaths))
            # paths += ((len(options) * count) - 1)
            print(curPaths, ", for", current, ", num paths:", paths)
        print()

print("num paths:", paths)