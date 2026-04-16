import sys
input = sys.stdin.readline

S = list(input().strip())
i = 0
stack = []

while i < len(S):
    if S[i] not in [' ','<']:
        stack.append(S[i])
        i += 1
    else:
        while stack:
            print(stack.pop(), end="")
        if S[i] == '<':
            while S[i] != '>':
                print(S[i], end = "")
                i += 1
        print(S[i], end="")
        i += 1
while stack:
    print(stack.pop(), end="")