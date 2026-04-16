import sys
input = sys.stdin.readline
while True:
    string = list(input())
    if string[0] == ".":
        break
    stack = []
    isVPS = "yes"
    for PS in string:
        if PS == '(':
            stack.append(PS)
        elif PS == '[':
            stack.append(PS)
        elif PS == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                isVPS = "no"
                break
        elif PS == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                isVPS = "no"
                break
    if stack:
        isVPS = "no"
    print(isVPS)