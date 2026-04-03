import sys
input = map(int, sys.stdin.read().split())

N = next(input)
stack = []
score = 0
for i in range(N):
    if next(input):
        AT = [next(input),next(input)-1]
        stack.append(AT)
        if stack[-1][1] == 0:
            f = stack.pop()
            score += f[0]
    else:
        if stack:
            stack[-1][1] -= 1
            if stack[-1][1] == 0:
                f = stack.pop()
                score += f[0]
print(score)