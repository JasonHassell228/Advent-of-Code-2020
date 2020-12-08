f = open("input", "r")
original = []
for line in f.readlines():
    original.append(line)
tries = 0 # Number of nop's changed to jmp's or vice versa
succeeded = 0

while not succeeded:
    print("restarting loop")
    inCopy = original.copy()
    lines = []
    explLines = [] # Explored lines
    acc = 0
    currLine = 0
    count = 0
    for line in inCopy:
        cmd = line.split()[0]
        # print("count:", count)

        if count == tries:
            if cmd == 'nop':
                new = 'jmp'
                new += " " + line.split()[1] + "\n"
                lines.append(new)
                # print("switching", line, "for", new, "at", tries)
            elif cmd == 'jmp':
                new = 'nop'
                new += " " + line.split()[1] + "\n"
                lines.append(new)
                # print("switching", line, "for", new, "at", tries)
            else:
                lines.append(line)
        else:
            lines.append(line)
        count += 1
    # print("lines len:", len(lines))
    while True:
        if currLine not in explLines:
            explLines.append(currLine)
        else:
            print("repeating on line", currLine)
            print("acc:", acc)
            tries += 1
            print("trying again, current tries:", tries)
            break
        # print("trying to get cmd from line", currLine)
        if (currLine < len(lines)):
            cmd = lines[currLine].split()[0] # Current command
        else:
            cmd = ""
        # print("cmd:", cmd)
        if cmd == 'nop':
            # print("no op")
            currLine += 1
        elif cmd == 'acc':
            add = int(lines[currLine].split()[1])
            # print("add", add)
            acc += add
            currLine += 1
        elif cmd == 'jmp':
            jmp = int(lines[currLine].split()[1])
            # print("jumping forward", jmp, "lines")
            currLine += jmp
        else:
            print("-------------------------------------- terminated -------------------------------------------")
            print("acc", acc)
            succeeded = 1
            break
