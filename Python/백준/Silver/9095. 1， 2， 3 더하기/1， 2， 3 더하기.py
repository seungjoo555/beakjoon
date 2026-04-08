T = int(input())
hab = [0,1,2,4]+[0]*(9)
def cal(n):
    for i in range(4,n+1):
        hab[i] = hab[i-1]+hab[i-2]+hab[i-3]
    print(hab[n])

for _ in range(T):
    n = int(input())
    cal(n)