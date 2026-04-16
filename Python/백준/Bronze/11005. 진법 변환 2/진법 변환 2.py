N, B = map(int, input().split())
alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

zin = ""

while N != 0:
    zin = str(alpha[N % B]) + zin
    N //= B

print(zin)