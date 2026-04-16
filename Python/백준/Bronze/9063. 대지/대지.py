import sys
input = sys.stdin.readline

N = int(input())
x, y = map(int, input().split())
xMax, yMax = x, y
xMin, yMin = x, y
for _ in range(N-1):
    x, y = map(int, input().split())
    if x > xMax: xMax = x
    if y > yMax: yMax = y
    if xMin > x: xMin = x
    if yMin > y: yMin = y
print((xMax-xMin)*(yMax-yMin))