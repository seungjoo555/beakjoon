N = int(input())
X = list(map(int, input().split()))
xSort = list(set(X))
xSort.sort()
xW = [i for i in range(len(xSort))]
xkey = dict(zip(xSort, xW))
for i in range(N):
    X[i] = xkey[X[i]]
print(' '.join(map(str ,X)))