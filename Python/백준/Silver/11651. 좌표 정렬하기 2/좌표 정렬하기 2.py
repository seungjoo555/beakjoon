import sys
N = int(input())
coor = map(int, sys.stdin.read().split())
coor1 = [[a, b] for a, b in zip(coor, coor)]
coor1.sort(key=lambda x:(x[1], x[0]))
for a, b in coor1:
    print(a, b)


