import sys

input = sys.stdin.readline
number = int(input())

for i in range(number*2-1):
    if i < number:
        print("*" * (i + 1) + " " * ((number * 2) - ((i + 1) * 2)) + "*" * (i + 1))
    if i >= number:
        print("*" * (number + (number - i -1)) + " " * (((i + 1) - number) * 2) + "*" * (number + (number - i -1)))