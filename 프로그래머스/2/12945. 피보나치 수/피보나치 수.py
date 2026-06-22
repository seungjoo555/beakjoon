def solution(n):
    fi = [0, 1]
    for i in range(2, n+1):
        a = fi[0] + fi[1]
        fi[0] = fi[1]
        fi[1] = a
    answer = fi[1] % 1234567
    return answer