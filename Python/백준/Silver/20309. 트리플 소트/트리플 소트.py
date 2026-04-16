import sys

n = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))
message = "YES"
for i in range(n//2):
    if list[(i*2)+1]%2 != 0:
        message = "NO"
        break
print(message)