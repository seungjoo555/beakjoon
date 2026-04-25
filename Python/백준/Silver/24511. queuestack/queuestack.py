import sys
from collections import deque

input = sys.stdin.readline

# 1. 입력 받기
n = int(input())
a = list(map(int, input().split()))  # 0: 큐, 1: 스택
b = list(map(int, input().split()))  # 초기 원소
m = int(input())
c = list(map(int, input().split()))  # 삽입할 원소들

# 2. 큐인 자료구조의 원소만 덱에 담기
# 큐는 먼저 들어간 게 먼저 나오므로, 연결된 큐들을 하나의 큰 덱으로 처리
q = deque()
for i in range(n):
    if a[i] == 0:
        q.append(b[i])

# 3. 새로운 원소 삽입 및 출력
# 큐가 하나도 없을 경우 삽입한 원소가 그대로 출력됨
for x in c:
    q.appendleft(x)
    print(q.pop(), end=' ')