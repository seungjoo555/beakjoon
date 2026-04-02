N = int(input())
bag = []
for i in range(N//5+1):
    for j in range(N//3+1):
        if N == ((5*i) + (3*j)):
            bag.append(i+j)
if len(bag):
    print(min(bag))
else:
    print(-1)