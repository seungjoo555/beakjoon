def solution(data, ext, val_ext, sort_by):
    answer = []
    col = {"code":0,"date":1,"maximum":2,"remain":3}
    k1 = col[ext]
    k2 = col[sort_by]
    for d in data:
        if d[k1] < val_ext:
            answer.append(d)
    answer.sort(key=lambda x : x[k2])
    return answer