import sys
input = sys.stdin.readline

A = input().strip().split()
A[0] = int(A[0][::-1])
A[1] = int(A[1][::-1])
print(max(A))