M = int(input())
count = 0
start = 1
end = 1
sum = 1
while end < M+1:
    if sum == M: count += 1
    if sum > M:
        sum -= start
        start += 1
    else:
        end += 1
        sum += end
print(count)