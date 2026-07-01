def solution(my_string):
    answer = 0
    for s in my_string:
        if ord(s) > 122 or ord(s) < 65:
            answer += int(s)
    return answer