n = int(input())
pibo = [0,1]+[0]*(n-1)
for i in range(2, len(pibo)):
    pibo[i] = pibo[i-1] + pibo[i-2]
print(pibo[n])