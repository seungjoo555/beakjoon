import sys

a, b = map(int, input().split())
numList1 = []
numList2 = []
for i in range(a):
    numList1.append(list(map(int, sys.stdin.readline().split())))
for i in range(a):
    numList2.append(list(map(int, sys.stdin.readline().split())))
for i in range(a):
    for j in range(b):
        numList1[i][j] = numList1[i][j] + numList2[i][j]
        print(numList1[i][j], end=" ")
    print()