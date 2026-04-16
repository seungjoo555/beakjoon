t = int(input())

for _ in range(t):
    n = int(input())
    res = 1
    for i in range(1, n+1):
        res *= i
    res = str(res)
    for j in range(-1, -len(res)-1, -1):
        if res[j] != '0':
            print(res[j])
            break