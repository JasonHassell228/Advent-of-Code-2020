f = open("input", "r")
# f = open("test", "r")

# Searching for 88,311,122
inp = []
sum = 0
num = 88311122
count = 0
count2 = 0
done = 0
for line in f.readlines():
    inp.append(int(line))
while not done:
    for i in inp[count:]:
        # print("i:", i, "sum:", sum)
        if sum < num:
            sum += i
            count2 += 1
        elif sum == num:
            y = 0
            for x in inp[count:count + count2]:
                y += x # Double checking answer
            print("found", sum, ",", "count", count, "count2", count2, inp[count:count + count2], y)
            print("answer:", min(inp[count:count + count2]) + max(inp[count:count + count2]))
            done = 1
            break
        else:
            print("couldn't find sum at", count, ", resetting")
            count += 1
            count2 = 0
            sum = 0
            break
