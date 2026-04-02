N = int(input())
bag = 0
for i in range(N//5, -1, -1):
    for j in range(N//3+1):
        if N == ((5*i) + (3*j)):
            bag = i+j
    if bag:
        print(bag)
        break
else:
    print(-1)