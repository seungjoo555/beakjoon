def solution(babbling):
    answer = 0
    for s in babbling:
        if len(s) > 10:
            continue
        joker = ["aya", "ye", "woo", "ma"]
        for i in range(4):
            if len(s) >= 2 and s[:2] in joker:
                joker.remove(s[:2])
                s = s[2:]
            elif len(s) >= 3 and s[:3] in joker:
                joker.remove(s[:3])
                s = s[3:]
        if s == "":
            answer += 1
    return answer