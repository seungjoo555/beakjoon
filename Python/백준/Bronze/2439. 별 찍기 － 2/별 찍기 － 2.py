import sys

x = int(sys.stdin.readline())

for i in range(x):
    print(" " * (x-(i+1)) + "*" * (i+1))