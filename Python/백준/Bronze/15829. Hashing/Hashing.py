import sys
n = int(sys.stdin.readline())
str = sys.stdin.readline().strip()
s = 0
for i in range(n):
    s += (ord(str[i])-96)*(31**i)%1234567891
print(s%1234567891)