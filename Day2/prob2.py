f = open("input", "r")
passwords = []
for line in f.readlines():
    info = line.split()
    min = info[0].split("-")[0]
    max = info[0].split("-")[1]
    letter = info[1][0]
    password = info[2]
    
    if (password[int(min)-1] == letter and password[int(max)-1] != letter):
        passwords.append(password)
    elif (password[int(min)-1] != letter and password[int(max)-1] == letter):
        passwords.append(password)

print(len(passwords))