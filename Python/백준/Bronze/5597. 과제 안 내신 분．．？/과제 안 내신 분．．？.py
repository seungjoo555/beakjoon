import sys

numList = list(map(int, sys.stdin.read().splitlines()))

for a in range(1,31):
    if numList.count(a) == 0:
        print(a)