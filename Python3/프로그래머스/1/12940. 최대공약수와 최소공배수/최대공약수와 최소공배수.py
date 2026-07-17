def solution(n, m):
    answer = []
    if n > m: n, m = m, n
    for i in range(n, 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    for j in range(1, n+1):
        if (m * j) % n == 0:
            answer.append(m * j)
            break
    return answer