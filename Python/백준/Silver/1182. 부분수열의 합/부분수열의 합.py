N, S = map(int, input().split())
s_list = list(map(int, input().split()))
count = 0
def s(sum, n):
    global count
    if n == N:
        if sum == S:
            count+=1
        return
    # print(s_list[n])
    s(sum, n+1)
    sum += s_list[n]
    # print(sum)
    s(sum, n+1)
    
s(0, 0)
if S == 0:
    count -= 1
print(count)
            