import math
def solution(s):
    l = (len(s)-1)/2
    return s[int(l):math.ceil(l)+1]