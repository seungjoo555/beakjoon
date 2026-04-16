h, m = map(int, input().split())
i = m - 45

if i >= 0:
    m = i
    print(h,m)
elif i < 0:
    m = 60 + i
    if h == 0:
        h = 23
    else:
        h -= 1
    print(h,m)