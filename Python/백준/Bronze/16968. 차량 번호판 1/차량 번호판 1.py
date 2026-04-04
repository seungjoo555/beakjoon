import sys
a = sys.stdin.readline().strip()
c = 26
d = 10
res = 0
if a[0] == 'c': res = c
else: res = d
for i in range(1, len(a)):
    if a[i] == 'c' and a[i-1] == 'c':
        res *= c-1
    elif a[i] == 'd' and a[i-1] == 'd':
        res *= d-1
    elif a[i] == 'c':
        res *= c
    else:
        res *= d
print(res)