def solution(a, b):
    if a > b:
        a, b = b, a
    answer = a
    for i in range(a+1, b+1):
        answer += i
    return answer