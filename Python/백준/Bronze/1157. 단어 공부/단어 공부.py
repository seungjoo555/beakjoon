import sys
input = sys.stdin.readline
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
S = (input())
S = S.upper()
check = []

for ch in alpha:
    check.append(S.count(ch))

if check.count(max(check)) > 1:
    print('?')
else:
    print(alpha[check.index(max(check))])