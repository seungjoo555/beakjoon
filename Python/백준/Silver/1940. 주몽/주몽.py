import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
itemList = list(map(int, input().split()))

sCount = 0
if M > 200000:
    print(sCount)
else:
    for i in range(N-1):
        if itemList[i] < M:
            sCount += itemList[i+1:].count(M - itemList[i])
    print(sCount)