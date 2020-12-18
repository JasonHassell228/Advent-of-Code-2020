f = open("input", "r")
# f = open("test", "r")
# f = open("test2", "r")
# f = open("simpletest", "r")

allColours = {} # For all colours

for line in f.readlines():
    colourDict = {} # Dict for each individual colour
    words = line.split()
    mainColour = words[0] + " " + words[1]
    index = 4
    for i in words[4:]:
        if index >= len(words):
            break
        else:
            num = words[index]
            if num == "no":
                continue # No bags for this colour
            else:
                num = int(num)
            colour = words[index + 1] + " " + words[index + 2]
            index += 4
            colourDict[colour] = num # Maps colour to number of bags of this colour
    allColours[mainColour] = colourDict # Maps individual colour to dict of colours contained in bag

explored = []
numBags = 0 # Number of colours that can contain at least one shiny gold bag

def recurse(allColours, values, numBags, preVal):
    subTotal = 0
    if not values:
        return 0
    for i in values:
        curVal = preVal * values.get(i)
        retval = recurse(allColours, allColours.get(i), numBags, curVal)
        subTotal += retval
        subTotal += curVal
    return subTotal

values = allColours.get("shiny gold")
print("initial values:", values)
numBags += recurse(allColours, values, numBags, 1)
print("numBags:", numBags)