def moveSlope(x,y,list,row):
    if list[y][x] == "#":
        return True
    return False


def traverseSlopes(incrX, incrY, list):
    currentX = 0
    currentY = 0
    treecount = 0

    for i in range(len(list)):
        if currentX + incrX > len(list[i]) - 1:
            currentX = currentX + incrX - len(list[i]);
        else:
            currentX += incrX

        if currentY + incrY > (len(list)-1):
            break;
        else:
            currentY += incrY
        if moveSlope(currentX,currentY, list, i):
            treecount += 1
    return treecount

with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))

    print(traverseSlopes(1,1,list) * traverseSlopes(3,1,list) * traverseSlopes(5,1,list) * traverseSlopes(7,1,list) * traverseSlopes(1,2,list))

