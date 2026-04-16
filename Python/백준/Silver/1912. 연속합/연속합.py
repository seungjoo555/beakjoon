import sys
n = int(input())
input = list(map(int, sys.stdin.read().split()))
yul = [0]*n
yul[0] = input[0]
for i in range(1, n):
    yul[i] = max(input[i], yul[i-1]+input[i])

print(max(yul))
    

