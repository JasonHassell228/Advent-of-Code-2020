f = open("input", "r")
# f = open("test", "r")
# f = open("test2", "r")

inp = []
diff1 = 0
diff2 = 0
diff3 = 0

for line in f.readlines():
    for i in line.split():
        inp.append(int(line))
print(inp)
inp.sort()
inp.append(inp[-1] + 3)
print(inp)
inp.append(0)
inp.sort()
print(inp)

for i in range(len(inp) - 1):
    # print("diff of", inp[i + 1], inp[i])
    diff = inp[i + 1] - inp[i]
    if diff == 1:
        diff1 += 1
    elif diff == 2:
        diff2 += 1
    elif diff == 3:
        diff3 += 1
    else:
        print("Something happened")
print(diff1, diff2, diff3)
print(diff1 * diff3)