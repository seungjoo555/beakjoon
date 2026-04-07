N = int(input())

dpList = [0] * (N+1)
for i in range(2,N+1):
    a = dpList[i-1]
    if i % 3 == 0:
        a = min(dpList[i//3], a)
    if i % 2 == 0:
        a = min(dpList[i//2], a)
    dpList[i] = a+1

print(dpList[N])