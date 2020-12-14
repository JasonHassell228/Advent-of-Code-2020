f = open("input", "r")
# f = open("test", "r")
preLen = 25
# preLen = 5
preamble = []
count = 0
for line in f.readlines():
    # print("pre", preamble, "count", count)
    if len(preamble) < preLen:
        preamble.append(int(line))
    else:
        current = int(line)
        done = 0
        iCt = 0
        for i in preamble:
            if done:
                break
            jCt = 0
            for j in preamble:
                # print("i, j:", iCt, jCt)
                if done:
                    break
                if iCt != jCt:
                    # print("trying", i, "+", j, "=", i + j, "for", current)
                    if (i + j) == current:
                        print("yes,", i, "+", j, "=", current)
                        done = 1
                jCt += 1
            iCt += 1
        if not done:
            print("no i + j found for", current)
        preamble[count] = int(line)
        count = (count + 1) % preLen
print(preamble)