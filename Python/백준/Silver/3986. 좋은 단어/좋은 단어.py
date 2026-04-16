import sys

input = sys.stdin.readline

N = int(input())
count = 0
for _ in range(N):
    stack = []
    goodWord = list(input().strip())
    for word in goodWord:
        if len(stack) < 1:
            stack.append(word)
        else:
            if word == stack[-1]:
                stack.pop()
            else:
                stack.append(word)
    if len(stack) == 0:
        count += 1
print(count)