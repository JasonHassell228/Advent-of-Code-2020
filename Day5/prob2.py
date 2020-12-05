f = open("input", "r")
current = []
valid = 0
for line in f.readlines():
    # print(line)
    if line == "\n":
        print("new passport for", current)
        if not ('byr' not in current or 'iyr' not in current or 'eyr' not in current or 'hgt' not in current or 'hcl' not in current or 'ecl' not in current or 'pid' not in current):
            valid += 1

        current = []
    print("currently processing", line)
    for i in line.split():
        t = i[:3]
        if t == 'byr':
            if int(i[4:]) < 1920 or int(i[4:]) > 2002:
                continue
            print("keep byr")
        if t == 'iyr':
            if int(i[4:]) < 2010 or int(i[4:]) > 2020:
                continue
            print("keep iyr")
        if t == 'eyr':
            if int(i[4:]) < 2020 or int(i[4:]) > 2030:
                continue
            print("keep eyr")
        if t == 'hgt':
            if i[4:-2] == '':
                print("shits fucked")
                continue
            if i[-2:] == 'cm':
                if int(i[4:-2]) < 150 or int(i[4:-2]) > 193:
                    continue
            elif i[-2:] == 'in':
                if int(i[4:-2]) < 59 or int(i[4:-2]) > 76:
                    continue
            print("keep hgt")
        if t == 'hcl':
            count = 0
            bad = 0
            if i[4:][0] != '#':
                print("bad hcl, no hash")
                continue
            for d in i[4:][1:]:
                print("d", d)
                if d not in {'a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                    print("bad hcl, bad chars", d)
                    bad = 1
                count += 1
            if count != 6 or bad > 0:
                print("bad hcl, bad count/chars")
                continue
            print("keep hcl")
        if t == 'ecl':
            if len(i[4:]) != 3:
                print("ecl bad:", i[4:])
            if i[4:] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                continue
            print("keep ecl")
        if t == 'pid':
            if len(str(i[4:])) != 9:
                continue
            for i in i[4:]:
                if i not in {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}:
                    continue
            print("keep pid")
        # print("splitting:", t, i[4:])
        current.append(t)
    
print(valid)
    # print(line.split()[0])
