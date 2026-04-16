N, K = map(int, input().split())

a = 1
b = 1
c = 1
for i in range(N, 1, -1):
    a *= i
for j in range(1, N-K+1):
    b *= j
for k in range(1, K+1):
    c *= k

print(a//(b*c))