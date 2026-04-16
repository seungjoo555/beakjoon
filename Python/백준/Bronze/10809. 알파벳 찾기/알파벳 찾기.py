import sys
input = sys.stdin.readline

alpha = [-1] * 26

S = list(input().strip())

for i in range(len(S)):
    if alpha[ord(S[i])-97] != -1:
        continue
    alpha[ord(S[i])-97] = i

for n in alpha:
    print(n, end=" ")