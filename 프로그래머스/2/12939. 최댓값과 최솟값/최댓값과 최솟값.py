def solution(s):
    sList = list(map(int, s.split()))
    answer = ' '.join([str(min(sList)), str(max(sList))])
    return answer