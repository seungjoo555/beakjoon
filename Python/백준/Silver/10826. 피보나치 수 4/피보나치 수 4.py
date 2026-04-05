n = int(input())
pibo = [0, 1]
if n <= 1: print(n)
else:
    for _ in range(n-1):
        temp = pibo[0] + pibo[1]
        pibo[0] = pibo[1]
        pibo[1] = temp
    print(pibo[1])