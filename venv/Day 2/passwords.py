
def findLetterOccurance(letter, password):
    occ = 0
    for p in password:
        if p == letter:
            occ += 1
    return occ


def isvalid(rules, password):
    [rule, letter] = rules.split(' ')
    [mini, maxi] = rule.split('-')

    occ = findLetterOccurance(letter, password)
    if occ <= int(maxi) and int(mini) <= occ:
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
