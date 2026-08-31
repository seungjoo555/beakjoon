def solution(arr, queries):
    answer = []
    for a, b, c in queries:
        t = [i for i in arr[a:b+1] if i > c]
        if t:
            answer.append(min(t))
        else:
            answer.append(-1)
        
    return answer