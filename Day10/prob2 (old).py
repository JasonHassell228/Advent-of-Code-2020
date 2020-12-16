# f = open("input", "r")
f = open("test", "r")
# f = open("test2", "r")

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
        if not curPaths:
            curPaths = options
        else:
            prevPaths = curPaths
            curPaths = options
        count = 0
        if not prevPaths:
            paths = paths * len(options)
        else:
            for k in prevPaths:
                if inp[i] >= k:
                    count += 1
            paths *= count
            print("count:", count, "prev", prevPaths, "len", len(options))
            # paths += ((len(options) * count) - 1)
            print(options, ", for", inp[i], ", num paths:", paths)
        print()

print("num paths:", paths)