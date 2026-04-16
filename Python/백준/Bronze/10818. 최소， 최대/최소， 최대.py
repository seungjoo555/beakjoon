import sys

n = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))
max = list[0]
min = list[0]
for i in range(n):
    if list[i] > max:
        max = list[i]
    if list[i] < min:
        min = list[i]
print(min, max)