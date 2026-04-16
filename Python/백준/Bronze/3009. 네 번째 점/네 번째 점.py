list1 = [[],[]]
a, b = 0, 0
# b = [5, 7]
# c = [7, 5]
for i in range(3):
    j, k = map(int, input().split())
    list1[0].append(j)
    list1[1].append(k)
for i in range(3):
    if list1[0].count(list1[0][i]) == 1:
        a = list1[0][i]
    if list1[1].count(list1[1][i]) == 1:
        b = list1[1][i]
print(a, b)