import numpy as np

def findSolution(list):

    array = np.array(list)
    array = array.astype(int)

    joltscount = [0,0,0]

    prevsmallest = 0

    builtin = np.amax(array) + 3
    array = np.append(array, builtin)

    while(len(array) != 0):
        smallest = np.amin(array)
        joltscount[smallest-prevsmallest-1] += 1
        prevsmallest = smallest

        new = np.delete(array, np.where(array == smallest))
        array = new
    print(joltscount)
    print(joltscount[0]*joltscount[2])

with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))
    findSolution(list)

    # [1,2,3,6,9]
    # trywithout(1,[])