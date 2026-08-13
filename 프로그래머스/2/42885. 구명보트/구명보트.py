from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    qqq = deque(people)
    while qqq:
        big = qqq.pop()
        if len(qqq) > 0:
            if big + qqq[0] <= limit:
                qqq.popleft()
        answer += 1
    return answer