import heapq
import sys
input = sys.stdin.readline

N = int(input())
my_heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if len(my_heap):
            print(heapq.heappop(my_heap))
        else:
            print(0)
    else:
        heapq.heappush(my_heap, x)