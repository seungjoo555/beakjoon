def solution(s):
    answer = -1
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    if stack:
        answer = 0
    else:
        answer = 1
    return answer