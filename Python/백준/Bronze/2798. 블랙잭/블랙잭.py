import sys
inp = map(int, sys.stdin.read().split())
N = next(inp)
M = next(inp)
card = [*inp]
card.sort()
max = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            sum = card[i]+card[j]+card[k]
            if max < sum <= M:
                max = sum
            elif sum > M:
                break
print(max)