import sys

list = list(map(int,sys.stdin.read().splitlines()))
n = len(list)
max = 0
for i in range(n):
    if list[i] > max:
        max = list[i]
print(max)
print(list.index(max) + 1)