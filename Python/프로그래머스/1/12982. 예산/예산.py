def solution(d, budget):
    answer = 0
    sum = 0
    d.sort()
    for i in range(len(d)):
        sum += d[i]
        if sum > budget:
            answer = i
            break
    if sum == budget or sum < budget:
        answer = len(d)
    return answer