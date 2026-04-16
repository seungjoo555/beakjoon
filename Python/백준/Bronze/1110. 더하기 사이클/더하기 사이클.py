import sys
input = sys.stdin.readline

N = int(input())
checkN = N
count = 0

while True:
    a = N // 10 + N % 10
    N = (N % 10) * 10 + (a % 10)
    count += 1
    if N == checkN:
        break
print(count)