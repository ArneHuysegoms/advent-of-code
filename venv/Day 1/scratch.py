import csv

def findx(x, list):
    for e in list:
        if int(e) + int(x) == 2020:
            return int(e) * int(x)
    return 0


def findSolution(list):
    if len(list) != 0:
        head = list.pop()
        result = findx(head,list)
        if result != 0:
            print(result)
        else: findSolution(list)



with open('../../../../PycharmProjects/Advent_Of_Code/venv/Day 1/input.txt', 'r') as file:
    list = []
    for line in file:
        list.append(line.replace('\n', ''))

    findSolution(list)
