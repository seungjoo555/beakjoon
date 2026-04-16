import sys

n = int(sys.stdin.readline())
if n != 0:
    result = 1
    for i in range(1, n+1):
        result = result * i
    print(result)
else:
    print(1)