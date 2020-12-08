f = open("input", "r")

allColours = {} # For all colours

for line in f.readlines():
    colourDict = {} # Dict for each individual colour
    words = line.split()
    mainColour = words[0] + " " + words[1]
    # print(mainColour + ", len=", len(words))
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
            # print("num:", num, "colour:", colour, " | ", end='')
            index += 4
            colourDict[colour] = num # Maps colour to number of bags of this colour
    allColours[mainColour] = colourDict # Maps individual colour to dict of colours contained in bag
# print(allColours)

explored = []
numBags = 0 # Number of colours that can contain at least one shiny gold bag

# for key, value in allColours.items():
#     print(key, value)

def recurse(toSearch, valuesToSearch, numBags): # Helper function
    # if not valuesToSearch:
    #     return numBags
    for i in valuesToSearch:
        # print(valuesToSearch)
        print("values for", i, end=': ')
        print(toSearch.get(i))
        if not toSearch.get(i):
            print(i, "has no values, continuing")
            continue
        
        print("adding", valuesToSearch.get(i), "to numBags from", i)
        numBags += valuesToSearch.get(i)
        print("multiplying", valuesToSearch.get(i), "with", ) # Is this second loop below actually needed??
        for j in toSearch.get(i):
            nCopy = numBags
            print("numBags at start of loop:", nCopy)
            numBags += toSearch.get(i).get(j)
            print("adding", toSearch.get(i).get(j), "to numBags from", j)
            if toSearch.get(j): # Only recurse if there are options left to search
                print("recursing into", j, "from", i, "searching for", toSearch.get(j))
                print("multiplying", toSearch.get(i).get(j), "from", j, "with", toSearch.get(j))
                # numBags += toSearch.get(i).get(j) * recurse(toSearch, toSearch.get(j), numBags)
                numBags += toSearch.get(i).get(j) * recurse(toSearch, toSearch.get(j), nCopy)
            else:
                print("no bags for", j)
            # numBags = toSearch.get(i).get(j) * recurse(toSearch, toSearch.get(j), numBags)
            # toExplore.append(j)
        #     print("numbags for", j, ":", numBags)
        print("numbags subtotal:", numBags)
    print("\nending a recursion\n")
        
    return numBags

def recurseSearch(toSearch, numBags): # Recursively search through colours
    values = toSearch.get("shiny gold")
    print("shiny gold contains:", values)

    for i in values:
        print("value of", i, ":", values.get(i))
        print("recursing originally for", toSearch.get(i), "from", i, "(adding", values.get(i), "from", i, "to numBags, don't worry)")
        numBags += values.get(i) # First level of bags
        print("multiplying", values.get(i), "from", i, "with recursion into", toSearch.get(i))
        numBags += values.get(i) * recurse(toSearch, toSearch.get(i), values.get(i)) # Next levels of bags
    return numBags

numBags = recurseSearch(allColours, numBags)
print("numBags:", numBags)
