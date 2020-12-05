f = open("input", "r")
passwords = []
for line in f.readlines():
    info = line.split()
    min = info[0].split("-")[0]
    max = info[0].split("-")[1]
    letter = info[1][0]
    password = info[2]
        
    if (password.count(letter) <= int(max) and password.count(letter) >= int(min)):
        passwords.append(password)
        print("max: ", max, "min ", min, "letter ", letter, " occurrence ", password.count(letter))

print(len(passwords))