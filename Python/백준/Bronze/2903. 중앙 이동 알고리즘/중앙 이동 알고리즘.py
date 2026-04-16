import sys
input = sys.stdin.readline

N = int(input())

jum = 4

for i in range(0, N):
    jum += ((2 ** i) * ((2 ** i + 1) * 2)) + ((2 ** i) ** 2)
print(jum)