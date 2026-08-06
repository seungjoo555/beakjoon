def solution(n):
    answer = 0
    t = []
    while n > 0:
        trans = n % 3
        n = n // 3
        t.append(trans)
    print(t)
    for i in range(len(t)):
        answer += 3 ** i * t.pop()

    return answer