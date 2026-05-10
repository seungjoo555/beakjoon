def solution(n):
    subak = "수박" * (n//2) + "수"*(n&1)
    return subak