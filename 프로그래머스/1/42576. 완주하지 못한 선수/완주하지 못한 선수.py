def solution(participant, completion):
    answer = ''
    s1 = set(participant)
    p = dict.fromkeys(s1,0)
    for name in participant:
        p[name] += 1
    for name in completion:
        p[name] -= 1
    for name, value in p.items():
        if value == 1:
            answer = name
            break
    return answer