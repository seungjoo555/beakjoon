def solution(number):
    answer = 0
    s = len(number)
    for i in range(s-2):
        for j in range(i+1, s-1):
            for k in range(j+1, s):
                if (number[i] + number[j] + number[k]) == 0:
                    answer += 1
    return answer