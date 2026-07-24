def solution(food):
    res = []
    for i in range(1,len(food)):
        res.append(str(i)*(food[i]//2))
    answer = "".join(res) + "0" + "".join(res[::-1])
    return answer