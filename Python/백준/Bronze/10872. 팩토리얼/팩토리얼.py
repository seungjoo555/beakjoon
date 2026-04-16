import sys

x = int(sys.stdin.readline())
n = 1
for i in range(1, x+1):
    n = n * i
print(n)