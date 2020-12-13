with open('input.txt', 'r') as file:
    list = [0]
    for line in file:
        list.append(int(line.replace('\n', '')))

    list.sort()
    list.append(list[-1:][0] + 3)

    arrange = [1] + [0] * list[-1]
    for i in list[1:]:
        arrange[i] = arrange[i - 3] + arrange[i - 2] + arrange[i - 1]

    print(arrange[-1])