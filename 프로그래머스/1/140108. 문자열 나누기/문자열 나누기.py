def solution(s):
    answer = 0
    xC = 0
    nxC = 0
    nx = ''
    for i in range(len(s)):
        if xC == 0:
            x = x = s[i]
        if s[i] == x:
            xC += 1
        else:
            nxC += 1
        if xC == nxC:
            answer += 1
            xC = 0
            nxC = 0
    if xC != 0:
        answer += 1
    return answer