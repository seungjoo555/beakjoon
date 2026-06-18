def solution(n):
    answer = 1
    for i in range(1, n//2+1):
        c = i
        for j in range(i+1, n//2+2):
            c += j
            if c == n:
                answer += 1
            elif c > n:
                break
    return answer