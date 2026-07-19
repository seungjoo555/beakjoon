def solution(s):
    answer = ''
    word = s.split(' ')
    for i in range(len(word)):
        trans = ""
        for j in range(len(word[i])):
            if j & 1 == 0:
                trans += word[i][j].upper()
            else:
                trans += word[i][j].lower()
        word[i] = trans
    answer = " ".join(word)
    return answer