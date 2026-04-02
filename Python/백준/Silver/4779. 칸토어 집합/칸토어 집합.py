import sys

def getCantor(size):
    if size == 1: return '-'
    newSize = size // 3
    center = " " * newSize
    side = getCantor(newSize)
    return side + center + side


inp = map(int, sys.stdin.read().split())
for i in inp:
    print(getCantor(3**i))