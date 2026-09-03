def solution(n):
    answer = []
    while(True):
        answer.append(n)
        if n == 1:
            break
        if n & 1:
            n = 3 * n + 1
        else:
            n //= 2
    return answer