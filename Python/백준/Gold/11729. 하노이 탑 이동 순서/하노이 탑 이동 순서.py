import sys
n = int(sys.stdin.readline())
def top(n, start, end):
    if n == 1: return print(start, end)
    top(n-1, start, 6-(start+end))
    print(start, end)
    top(n-1, 6-(start+end), end)

print(2**n - 1)
top(n, 1, 3)