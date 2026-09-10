def solution(intStrs, k, s, l):
    answer = []
    for intS in intStrs:
        i = int(intS[s:s+l])
        if k < i:
            answer.append(i)
    return answer