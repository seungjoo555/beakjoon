N = int(input())

dpList = [0] * (N+1)
for i in range(2,N+1):
    a = []
    if i % 3 == 0:
        a.append(dpList[i//3])
    if i % 2 == 0:
        a.append(dpList[i//2])
    a.append(dpList[i-1])
    dpList[i] = min(a)+1
print(dpList[N])