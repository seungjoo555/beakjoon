import sys
input = sys.stdin.readline

xywh = list(map(int, input().split()))
min = xywh[0]
xywh.append(xywh[3] - xywh[1])
xywh.append(xywh[2] - xywh[0])
for i in xywh:
    if min > i:
        min = i
print(min)