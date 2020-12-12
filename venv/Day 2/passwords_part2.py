def isvalid(rules, password):
    [rule, letter] = rules.split(' ')
    [pos1, pos2] = rule.split('-')

    if (password[int(pos1)-1] == letter and password[int(pos2)-1] != letter) or (password[int(pos1)-1] != letter and password[int(pos2)-1] == letter):
        return True

def findSolution(list):
    count = 0
    for line in list:
        splitup = line.split(': ')
        if isvalid(splitup[0],splitup[1]):
            count += 1
    print(count)


with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))

    findSolution(list)
