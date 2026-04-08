import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a=b=0
array = []
while N>a and M>b:
    if A[a] < B[b]:
        array.append(A[a])
        a+=1
    else:
        array.append(B[b])
        b+=1
if a<N:
    array.extend(A[a:N])
if b<M:
    array.extend(B[b:M])

print(' '.join(map(str, array)))