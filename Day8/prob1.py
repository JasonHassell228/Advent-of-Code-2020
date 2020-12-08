f = open("input", "r")

currLine = 0
acc = 0
lines = []
explLines = [] # Explored lines
for line in f.readlines():
    lines.append(line)

while True:
    if currLine not in explLines:
        explLines.append(currLine)
    else:
        print("repeating on line", currLine)
        print("acc:", acc)
        break
    cmd = lines[currLine].split()[0] # Current command
    print(cmd)
    if cmd == 'nop':
        print("no op")
        currLine += 1
    elif cmd == 'acc':
        add = int(lines[currLine].split()[1])
        print("add", add)
        acc += add
        currLine += 1
    elif cmd == 'jmp':
        jmp = int(lines[currLine].split()[1])
        print("jumping forward", jmp, "lines")
        currLine += jmp
    else:
        print("-------------------------------------- terminated -------------------------------------------")
        break
