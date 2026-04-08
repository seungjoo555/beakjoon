def pibo(num):
    if fibo[num] == -1:
        fibo[num] = pibo(num-1) + pibo(num-2)
    return fibo[num]

n = int(input())
fibo = [0,1]+[-1]*(n-1)
print(pibo(n))