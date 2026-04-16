findPc = list(map(int, input().split()))
pc = [1, 1, 2, 2, 2, 8]

for i in range (6):
    print(pc[i]-findPc[i], end=" ")