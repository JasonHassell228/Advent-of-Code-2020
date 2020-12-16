# f = open("input", "r")
f = open("test", "r")
# f = open("test2", "r")

inp = []

for line in f.readlines():
    for i in line.split():
        inp.append(int(line))
inp.sort()
inp.append(inp[-1] + 3)
inp.append(0)
inp.sort()
print(inp)

def recurse(inp, paths, pos):
    lim = inp[pos] + 3
    options = []
    print("curr search", inp[pos:])
    for i in inp[pos:]:
        if i 
        options.append(i)
        
        
        
        if i == (inp[-1] + 3):
            paths += 1
        else:
            # print("pos", pos)
            if pos < (len(inp) - 1):
                paths += recurse(inp, paths, (pos + 1))
            else:
                break
        print()
    return paths

paths = recurse(inp, 1, 0)
print("num paths:", paths)