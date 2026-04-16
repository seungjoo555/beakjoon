import sys
input = sys.stdin.readline

N = int(input())
M = list(map(int, input().split()))
sum = 0
for i in M:
    sum += i / max(M) * 100

print(sum / N)