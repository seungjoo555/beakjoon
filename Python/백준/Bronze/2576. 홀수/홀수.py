import sys

list = list(map(int,sys.stdin.read().splitlines()))
n = len(list)
sum = 0
oddList = []
for i in range(n):
    if list[i] % 2 != 0:
        sum += list[i]
        oddList.append(list[i])
if sum != 0:
    oddList.sort()
    print(sum)
    print(oddList[0])
else:
    print(-1)    