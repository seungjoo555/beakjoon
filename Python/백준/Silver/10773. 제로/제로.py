import sys
input = map(int, sys.stdin.read().split())
K = next(input)
nist = []
sum = 0
for _ in range(K):
    n = next(input)
    if n != 0:
        nist.append(n)
        sum += n
    else:
        sum -= nist.pop()
print(sum)