import sys
input = map(int, sys.stdin.read().split())
K = next(input)
nist = []
for _ in range(K):
    n = next(input)
    if n != 0:
        nist.append(n)
    else:
        nist.pop()
print(sum(nist))