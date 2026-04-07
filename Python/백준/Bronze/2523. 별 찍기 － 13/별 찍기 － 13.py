import sys
n = int(sys.stdin.readline())
for i in range(n):
    print('*' * (1+i))
for i in range(n-1):
    print('*' * ((n-1)-i))