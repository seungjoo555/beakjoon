def solution(ingredient):
    answer = 0
    length = len(ingredient)-3
    i = 0
    stack = []
    for cur in ingredient:
        stack.append(cur)
        if stack[-4:] == [1,2,3,1]:
            answer += 1
            del stack[-4:]
    return answer