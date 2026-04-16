h, m = map(int, input().split())
c = int(input())
i = m + c
if i < 60:
    m = i
    print(h,m)
elif i >= 60:
    m = i % 60
    h += i//60
    if h > 23:
        h -= 24
    print(h,m)