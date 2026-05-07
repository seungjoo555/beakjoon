def solution(x):
    answer = True
    y = 0
    x = str(x)
    for i in range(len(x)):
        y += int(x[i])
    if int(x) % y != 0:
        answer = False
    return answer