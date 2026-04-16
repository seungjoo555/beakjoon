import sys
input = sys.stdin.readline

dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
sum = 0
A = list(input().strip())
for i in range(len(dial)):
    for a in A:
        if dial[i].find(a) != -1:
            sum += i+3
print(sum)