def so():
    N = int(input())
    dpList = [0] * (N+1)
    for i in range(2,N+1):
        dpList[i] = dpList[i-1]+1
        if i % 2 == 0:
            dpList[i] = min(dpList[i//2]+1, dpList[i])
        if i % 3 == 0:
            dpList[i] = min(dpList[i//3]+1, dpList[i])

    print(dpList[N])

so()