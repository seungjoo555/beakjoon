import sys
input = sys.stdin.read

numList = list(map(int, input().splitlines()))

for i in range(10):
    numList[i] = numList[i] % 42

for num in numList:
    if numList.count(num) > 1:
        for _ in range(numList.count(num) - 1):
            numList.remove(num)
print(len(numList))