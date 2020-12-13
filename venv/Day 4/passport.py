import re

def checkreqs(dict):
    if "byr" in dict and int(dict["byr"]) <= 2002 and 1920 <= int(dict["byr"]) and\
            "iyr" in dict and int(dict["iyr"]) <= 2020 and 2010 <= int(dict["iyr"]) and\
            "eyr" in dict and int(dict["eyr"]) <= 2030 and 2020 <= int(dict["eyr"]) and\
            "hgt" in dict and ((dict["hgt"][-2:] == "in" and int(dict["hgt"][:-2]) <= 76 and 59 <= int(dict["hgt"][:-2])) or (dict["hgt"][-2:] == "cm" and int(dict["hgt"][:-2]) <= 193 and 150 <= int(dict["hgt"][:-2]))) and\
            "hcl" in dict and re.search("^#([a-f0-9]){6}$",dict["hcl"]) is not None and \
            "ecl" in dict and (dict["ecl"] == "amb" or dict["ecl"] == "blu" or dict["ecl"] == "brn" or dict["ecl"] == "gry" or dict["ecl"] == "grn" or dict["ecl"] == "hzl" or dict["ecl"] == "oth") and \
            "pid" in dict and re.search("^\d{9}$",dict["pid"]) is not None :
        return True
    else:
        return False

def findSolution(list):
    count = 0
    fields = {}
    for line in list:
        if line == '':
            if checkreqs(fields):
                count += 1
            fields = {}
        else:
            fld = line.split(' ')
            for f in fld:
                [code, val] = f.split(':')
                if code in fields:
                    fields = {}
                else:
                    fields[code] = val
    if checkreqs(fields):
        count += 1
    print(count)



with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))

    findSolution(list)