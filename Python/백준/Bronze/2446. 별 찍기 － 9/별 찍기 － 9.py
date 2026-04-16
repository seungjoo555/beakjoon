import sys

input = sys.stdin.readline
number = int(input())

for i in range(number * 2 - 1):
    if i < number:
        print(" " * i + "*" * (number * 2 - (i * 2 + 1)))
    else:
        print(" " * ((number - 1) - ((i + 1) - number)) + "*" * (((i - (number - 1)) * 2) + 1))