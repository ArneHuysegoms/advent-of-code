
def findxy(x, y, list):
    for z in list:
        if int(x) + int(y) + int(z) == 2020:
            print(int(x) * int(y) * int(z))
            return int(x) * int(y) * int(z)

def findx(x, list):
    if len(list) != 0:
        head = list.pop(0)
        result = findxy(x, head, list)
        if result is not None and result != 0:
            return result
        findx(x, list)

def findSolution(list):
    if len(list) != 0:
        head = list.pop(0)
        new = list.copy()
        result = findx(head,new)
        if result is not None and result != 0:
            print(result)
        else: findSolution(list)

with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))

    findSolution(list)
