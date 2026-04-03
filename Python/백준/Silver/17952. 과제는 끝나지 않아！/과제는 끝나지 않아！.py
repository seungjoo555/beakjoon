import sys
input = sys.stdin.readline

N = int(input())
stack = []
score = 0
for i in range(N):
    AT = list(map(int, input().split()))
    if AT[0] != 0:
        AT[2] -= 1
        stack.append(AT)
    if stack:
        if AT[0] == 0:
            stack[-1][2] -= 1
        if stack[-1][2] == 0:
            f = stack.pop()
            score += f[1]
print(score)