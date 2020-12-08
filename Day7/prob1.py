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
print(allColours)

explored = []
numColours = 0 # Number of colours that can contain at least one shiny gold bag

for key, value in allColours.items():
    print(key, value)

def recurse(toSearch, valuesToSearch, expl): # Helper function
    if "shiny gold" in valuesToSearch:
        print("found shiny gold")
        return 1
    else:
        for i in valuesToSearch:
            if i not in expl:
                expl.append(i)
                if recurse(toSearch, toSearch[i], expl):
                    return 1
    return 0

def recurseSearch(toSearch, numColours): # Recursively search through colours
    for key, value in toSearch.items():
        if key not in explored:
            explored.append(key)

            print("values for", key, end=': ')
            for i in value:
                print(i, end=', ')
            print()
            
            print("recursing: ")
            expl = [] # Explored array for each colour to avoid cycles
            print("og", value)
            numColours += recurse(toSearch, value, expl)
    return numColours

numColours = recurseSearch(allColours, numColours)
print("numColours:", numColours)
