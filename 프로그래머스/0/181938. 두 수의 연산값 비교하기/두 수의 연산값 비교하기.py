def solution(a, b):
    string = str(a) + str(b)
    answer = int(string) if int(string) > 2*a*b else 2*a*b
    return answer