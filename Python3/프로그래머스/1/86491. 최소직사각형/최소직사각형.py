def solution(sizes):
    wM = 0
    hM = 0
    for w, h in sizes:
        if w < h: w, h = h, w
        if wM < w: wM = w
        if hM < h: hM = h
    answer = wM * hM
    return answer