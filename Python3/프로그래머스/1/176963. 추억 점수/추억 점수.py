def solution(name, yearning, photo):
    answer = []
    
    for people in photo:
        score = 0
        for saram in people:
            if name.count(saram):
                id = name.index(saram)
                score += yearning[id]
        answer.append(score)
    return answer