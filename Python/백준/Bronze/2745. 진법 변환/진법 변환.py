import sys
input = sys.stdin.readline
alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = input().split()
sum = 0
for i in range(len(N)):
    sum  += alpha.index(N[len(N)-(i+1)]) * (int(B)**i)
print(sum)