n = int(input())

for i in range(n):
    print(" "*(n-1-i)+"*"*(1+(i*2)))
for i in range(1, n):
    print(" "*(i)+"*"*((n-i)*2-1))