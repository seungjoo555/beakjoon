a = input()
check = []
stack = []
for t in a:
    if t == '(':
        stack.append(t)
    elif t == ')' and stack:
        stack.pop()
    elif t == ')' and len(stack) == 0:
        check.append(t)
print(len(check)+len(stack))