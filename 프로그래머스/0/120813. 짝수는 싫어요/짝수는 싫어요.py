def solution(n):
    answer = [i for i in range(1, n+1) if i&1 == 1]
    return answer