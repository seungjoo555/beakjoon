N = int(input())
length = N*4-3
sts = [[' ']*(length) for _ in range(length)]
def st(n, x, y):
    if n == 1:
        sts[length//2][length//2] = '*'
        return
    leng = n*4-3
    for i in range(leng):
        sts[y][x+i] = "*"
        sts[y+i][x] = "*"
        sts[y+(leng-1)][x+i] = "*"
        sts[y+i][x+(leng-1)] = "*"
    n = n-1
    x += 2
    y += 2
    st(n, x, y)
    return
st(N, 0, 0)
for star in sts:
    print(''.join(star))