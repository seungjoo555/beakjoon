def solution(k, score):
    answer = []
    ho = []
    for i in score:
        if len(ho) < k:
            ho.append(i)
            ho.sort(reverse = True)
        else:
            ho.append(i)
            ho.sort(reverse = True)
            ho.pop()
        answer.append(ho[-1])
    return answer