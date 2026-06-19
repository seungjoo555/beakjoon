def solution(n):
    i = n + 1
    a = str(format(n, 'b'))
    b = str(format(i, 'b'))
    while a.count('1') != b.count('1'):
        i += 1
        b = str(format(i, 'b'))
    answer = i
    return answer