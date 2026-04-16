import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

c = (V - A) / (A - B)
if c % 1 > 0:
    c = c + 1

print(int(c) + 1)