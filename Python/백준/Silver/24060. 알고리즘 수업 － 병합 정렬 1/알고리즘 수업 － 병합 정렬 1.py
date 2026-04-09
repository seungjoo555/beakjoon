import sys
N, K = map(int, input().split())
A = list(map(int, sys.stdin.readline().split()))
count = 1
def merge_sort(A, left, right):
    if left < right:
        mid = (left+right)//2
        merge_sort(A, left, mid)
        merge_sort(A, mid+1, right)
        merge(A, left, mid, right)

def merge(A, left, mid, right):
    global count
    i = left
    j = mid+1
    t = 0
    tmp = [0] * (right-left+1)
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            t, i = t+1, i+1
        else:
            tmp[t] = A[j]
            t, j = t+1, j+1
    while i <= mid:
        tmp[t] = A[i]
        t, i = t+1, i+1
    while j <= right:
        tmp[t] = A[j]
        t, j = t+1, j+1
    i = left
    t = 0
    while i <= right:
        A[i] = tmp[t]
        if count == K:
            print(tmp[t])
        count += 1
        t, i = t+1, i+1

merge_sort(A, 0, N-1)
if count <= K:
    print(-1)