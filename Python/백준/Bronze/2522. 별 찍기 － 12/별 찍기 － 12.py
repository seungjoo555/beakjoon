import sys
n = int(sys.stdin.readline())
for i in range(n):
    print(' ' * ((n-1)-i)+ '*' * (1+i))
for i in range(n-1):
    print(' ' * (1+i)+ '*' * ((n-1)-i))
