f = open("input", "r")
grid = []
height = 0
for line in f.readlines():
    grid.append(line.split()[0])
    width = len(line.split()[0])
    height += 1
print(grid)
heightT = len(grid)
inX = 0
inY = 0
trees = 0
for i in grid:
    inX += 3
    inY += 1
    print(inX, inY, "width:", width, "height:", heightT)
    if inX >= width:
        inX = (inX % width)
        print("newline, new inX: ", inX, "trees: ", trees)
    if inY >= heightT:
        break
    print("looking for tree at pos", inX, "of", grid[inY])
    if grid[inY][inX] == '#':
        trees += 1

print(trees)
