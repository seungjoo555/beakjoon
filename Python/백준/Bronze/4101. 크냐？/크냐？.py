import sys
a, b = None, None
while a != 0 and b != 0:
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        print("Yes")
    elif a == b == 0:
        break
    else:
        print("No")