def solution(brown, yellow):
    answer = []
    for i in range((brown-2)//2, 2, -1):
        if answer:
            break
        for j in range(i+1):
            if j > i:
                break
            if i*j == (brown+yellow) and (i-2)*(j-2) == yellow:
                answer.append(i)
                answer.append(j)
                break
    return answer