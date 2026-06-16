def solution(s):
    s = s.lower()
    if ord(s[0]) > 90:
        s = s.replace(s[0], chr(ord(s[0])-32), 1)
    for i in range(1, len(s)):
        if s[i] != " " and s[i-1] == " " and ord(s[i]) > 96:
            s = s[:i] + chr(ord(s[i])-32) + s[i+1:]
    return s