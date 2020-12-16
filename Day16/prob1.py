f = open("input", "r")
# f = open("test", "r")

inp = []
ranges = []
for line in f.readlines():
    inp.append(line)

l = 0
newlines = []
for line in inp:
    if line == "\n":
        print("newline at", l)
        newlines.append(l)
    l += 1

for line in inp[:newlines[0]]:
    r = []
    r.append(line.split()[-3:][0].split('-')[0])
    r.append(line.split()[-3:][0].split('-')[1])
    ranges.append(r)
    r = []
    r.append(line.split()[-3:][2].split('-')[0])
    r.append(line.split()[-3:][2].split('-')[1])
    ranges.append(r)

# print("ranges:", ranges)


# for line in inp[21:23]:
#     print(line)
invalid = {}
invalidVals = []
lineNum = 0
for line in inp[newlines[1] + 2:]:
    for i in line.split(','):
        i = int(i)
        valid = False
        for r in ranges:
            # print("checking", i, "for range", r, "on line", lineNum)
            if i >= int(r[0]) and i <= int(r[1]): # Within a range
                # Number is valid for at least 1 range, move on
                # print(i, "within range", r, ", valid")
                valid = True
                break
        if not valid:
            # i in this line is not valid, therefore entire line is invalid
            invalLine = newlines[1] + 3 + lineNum
            invalid[invalLine] = invalLine
            # print("line", invalLine, "invalid because of", i)
            invalidVals.append(i)
    lineNum += 1

print("invalid lines:", end=' ')
temp = []
for i in invalid:
    temp.append(i)
print(temp)

print("ticket scanning error rate:", sum(invalidVals))
