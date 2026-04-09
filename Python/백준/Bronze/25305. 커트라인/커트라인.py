import sys
N, K = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.read().split()))
x.sort(reverse=True)
print(x[K-1])