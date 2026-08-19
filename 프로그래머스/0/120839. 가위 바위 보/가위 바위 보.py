def solution(rsp):
    answer = ''
    w = []
    for ch in rsp:
        if ch == '2':
            w.append('0')
        elif ch == '0':
            w.append('5')
        elif ch == '5':
            w.append('2')
    answer = ''.join(w)
    return answer