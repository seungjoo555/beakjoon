import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, S = input().strip().split()
    for s in S:
        for _ in range(int(n)):
            print(s, end="")
    print()