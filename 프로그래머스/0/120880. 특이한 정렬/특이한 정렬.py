def solution(numlist, n):
    answer = []
    while numlist:
        check = 0
        min = n - numlist[0] if n > numlist[0] else numlist[0] - n
        for i in range(1, len(numlist)):
            distance = n - numlist[i] if n > numlist[i] else numlist[i] - n
            if min > distance:
                min = distance
                check = i
            elif min == distance:
                if numlist[i] > numlist[check]:
                    check = i
        answer.append(numlist.pop(check))
    return answer