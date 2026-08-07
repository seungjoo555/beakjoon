from collections import Counter
def solution(k, tangerine):
    answer = 0
    check = 0
    count = Counter(tangerine)
    temp = sorted(count.values(), reverse = True)
    for j in temp:
        answer += 1
        check += j
        if k <= check:
            break
    return answer