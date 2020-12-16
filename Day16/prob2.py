f = open("input", "r")
# f = open("test", "r")
# f = open("test2", "r")

inp = []
ranges = []
newRanges = []
for line in f.readlines():
    inp.append(line)

l = 0
newlines = []
for line in inp:
    if line == "\n":
        newlines.append(l)
    l += 1

for line in inp[:newlines[0]]:
    newR = []
    r = []
    r.append(int(line.split()[-3:][0].split('-')[0]))
    r.append(int(line.split()[-3:][0].split('-')[1]))
    ranges.append(r)
    newR.append(r)
    r = []
    r.append(int(line.split()[-3:][2].split('-')[0]))
    r.append(int(line.split()[-3:][2].split('-')[1]))
    ranges.append(r)
    newR.append(r)
    newR.insert(0, line.split(':')[0])
    newRanges.append(newR)

invalidVals = []
invalidLines = []
lineNum = 0
for line in inp[newlines[1] + 2:]:
    for i in line.split(','):
        i = int(i)
        valid = False
        for r in ranges:
            if i >= int(r[0]) and i <= int(r[1]): # Within a range
                # Number is valid for at least 1 range, move on
                valid = True
                break
        if not valid:
            # i in this line is not valid, therefore entire line is invalid
            invalLine = lineNum
            invalidLines.append(invalLine)
            invalidVals.append(i)
    lineNum += 1

newInp = (inp[newlines[1] + 2:]).copy()
for i in reversed(invalidLines):
    newInp.remove(newInp[i])
options = {}
lineLen = len(newInp[0].split(","))
for i in newRanges:
    rangeName = i[0]
    options[rangeName] = list(range(lineLen))
for i in newInp:
    pass

for i in newInp:
    column = 0
    for j in i.split(','):
        j = int(j)
        for k in newRanges:
            # k[1][0] Range 1 min
            # k[1][1] Range 1 max
            # k[2][0] Range 2 min
            # k[2][1] Range 2 max
            if (j < k[1][0] or j > k[1][1]) and (j < k[2][0] or j > k[2][1]):
                if column in options[k[0]]:
                    options[k[0]].remove(column)
        column += 1

for k in options:
    for i in options:
        if len(options.get(i)) == 1:
            num = options.get(i)[0]
            for j in options:
                if j != i:
                    if num in options[j]:
                        options[j].remove(num)

print("end options:", options)
yourTicket = inp[newlines[0] + 2].split(',')
answer = 1
for i in options:
    if "departure" in i:
        print(i, options[i][0])
        answer *= int(yourTicket[options[i][0]])
print("answer:", answer)
