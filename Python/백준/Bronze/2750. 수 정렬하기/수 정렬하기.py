import sys
N = int(sys.stdin.readline())
number = list(map(int, sys.stdin.read().split()))
number.sort()
for i in number:
    print(i)
