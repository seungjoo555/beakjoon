from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
people = deque([i for i in range(1, N+1)])

print("<", end="")
for _ in range(N-1):
    people.rotate((K-1) * -1)
    print(people.popleft(), end = ", ")
print(f"{people[0]}>")