import sys

listNN = []
for i in range(9):
    listNN.append(list(map(int, sys.stdin.readline().split())))

max = listNN[0][0]
for i in range(len(listNN)):
    for j in range(len(listNN[i])):
        if listNN[i][j] > max:
            max = listNN[i][j]
for i in range(len(listNN)):
    for j in range(len(listNN[i])):
        if listNN[i][j] == max:
            x, y = i+1, j+1
print(max)
print(x, y)