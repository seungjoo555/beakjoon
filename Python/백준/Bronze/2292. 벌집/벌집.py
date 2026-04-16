N = int(input())
count = 0
i = 1
sum = 1
while True:
    if sum >= N:
        count = i
        break
    sum += 6 * i
    i += 1
print(count)