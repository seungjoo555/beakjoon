def solution(myString, pat):
    answer = 0
    a = myString.lower()
    b = pat.lower()
    if a.find(b) == -1:
        answer = 0
    else:
        answer = 1
    return answer