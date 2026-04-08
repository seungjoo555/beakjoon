T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    ho = [i for i in range(0,n+1)]
    for _ in range(k):
        for i in range(n):
            ho[i+1] = ho[i]+ho[i+1]
    print(ho[n])
