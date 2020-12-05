f = open("input", "r")
grid = []
height = 0
for line in f.readlines():
    grid.append(line.split()[0])
    width = len(line.split()[0])
    height += 1
heightT = len(grid)
inX = 0
inY = 0
trees = 0
for i in grid:
    inX += 1
    inY += 2
    if inX >= width:
        inX = (inX % width)
    if inY >= heightT:
        break
    if grid[inY][inX] == '#':
        trees += 1

print(trees)

# Did the different combinations manually