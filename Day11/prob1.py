f = open("input", "r")
# f = open("test", "r")

inp = []
for line in f.readlines():
    for i in line.split():
        inp.append(i)
# print(inp)
width = len(inp[0])
height = len(inp)

def getNeighbours(inp, inpCopy, row, column):
    center = inp[row][column]
    L = 0
    h = 0
    for i in range(row - 1, row + 2):
        for j in range(column - 1, column + 2):
            if i >= 0 and i < width and j >= 0 and j < height and (i != row or j != column):
                cur = inp[i][j]
                if cur == 'L':
                    L += 1
                elif cur == '#':
                    h += 1
    # RULES
    if center == 'L' and h == 0:
        temp = list(inpCopy[row])
        temp[column] = '#'
        inpCopy[row] = "".join(temp)
    elif center == '#' and h >= 4:
        temp = list(inpCopy[row])
        temp[column] = 'L'
        inpCopy[row] = "".join(temp)
    else:
        # Nothing changed, stable
        pass
    # RULES
    return inpCopy

iterations = 0
finished = 0
while not finished:
    inpCopy = inp.copy()
    for i in range(width):
        for j in range(height):
            inpCopy = getNeighbours(inp, inpCopy, i, j)
    print("iteration", iterations)
    if inp != inpCopy:
        inp = inpCopy.copy()
    else:
        finished = 1
        break # Done
    iterations += 1
print("finished at iteration", iterations)
h = 0
for i in inp:
    for j in i:
        if j == '#':
            h += 1
print(h, "occupied seats")
