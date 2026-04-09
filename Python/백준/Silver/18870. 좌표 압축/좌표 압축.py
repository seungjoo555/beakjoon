N = int(input())
X = list(map(int, input().split()))
xSort = list(set(X))
xSort.sort()
xW = [i for i in range(len(xSort))]
xkey = dict(zip(xSort, xW))
for i in X:
    print(xkey[i], end=' ')