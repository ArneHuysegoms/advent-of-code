bag = [0]
with open('testinput.txt') as fp:
    line = fp.readline()
    while line:
        bag.append(int(line.strip()))
        line = fp.readline()

bag.sort()
bag.append(bag[-1:][0]+3)

arrange = [1]+[0]*bag[-1]
for i in bag[1:]:
    arrange[i] = arrange[i-3] + arrange[i-2] + arrange[i-1]

print(f'\n\nPart 2\n{arrange[-1]}')