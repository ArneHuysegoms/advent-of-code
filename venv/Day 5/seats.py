import numpy as np
import math

def takelowerhalf(array):
    if len(array) == 1:
        return array
    else:
        return array[0:math.ceil((len(array)/2))]

def takeupperhalf(array):
    if len(array) == 1:
        return array
    else:
        return array[math.ceil(len(array)/2):len(array)]


def findSeat(string):
    rows = np.arange(128)
    cols = np.arange(8)
    for i in range(len(string)):
        if string[i] == 'F':
            rows = takelowerhalf(rows)
        if string[i] == 'B':
            rows = takeupperhalf(rows)
        if string[i] == 'L':
            cols = takelowerhalf(cols)
        if string[i] == 'R':
            cols = takeupperhalf(cols)
    return rows[0] * 8 + cols[0]



def findSolution(list):
    highestid = 0
    allids = np.arange(127*8+7)
    for line in list:
        currid = findSeat(line)
        new = np.delete(allids, np.where(allids == currid))
        allids = new
        if  highestid < currid:
            highestid = currid
    print(highestid)
    print(allids)


with open('input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))

    findSolution(list)