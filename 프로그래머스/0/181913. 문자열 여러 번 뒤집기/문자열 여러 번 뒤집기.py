def solution(my_string, queries):
    answer = my_string
    for i, j in queries:
        if i != 0:
            answer = answer[0:i] + answer[j:i-1:-1] + answer[j+1:]
        else:
            answer = answer[0:i] + answer[j::-1] + answer[j+1:]
    return answer