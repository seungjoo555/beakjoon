import sys
inp = map(int, sys.stdin.read().split())
N = next(inp)
K = next(inp)
coin = [*inp]
cCount = 0
for i in coin[-1::-1]:
    cCount += K // i
    K = K % i
    if K == 0:
        break
print(cCount)