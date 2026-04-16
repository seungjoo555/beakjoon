import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    stack = []
    isVPS = "YES"
    VPS = list(input())
    for PS in VPS:
        if PS == "(":
            stack.append(PS)
        elif PS == ")":
            if stack:
                stack.pop()
            else:
                isVPS = "NO"
                break
    if stack:
        isVPS = "NO"
    print(isVPS)