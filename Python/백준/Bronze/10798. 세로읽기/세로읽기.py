import sys
input = sys.stdin.read

A = input().splitlines()

for i in range(15):
    for j in range(5):
        if len(A[j]) > i:
            print(A[j][i], end="")