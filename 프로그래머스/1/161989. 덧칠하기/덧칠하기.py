def solution(n, m, section):
    answer = 0
    while section:
        roll = section[-1] - m
        while section:
            if section[-1] > roll:
                section.pop()
            else:
                break
        answer += 1
    return answer