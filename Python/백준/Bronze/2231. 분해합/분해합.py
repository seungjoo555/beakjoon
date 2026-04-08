N = int(input())

for i in range((N-(10*(len(str(N))))), N):
    seang = i
    seang += i//100000
    a = i%100000
    seang += a//10000
    a %= 10000
    seang += a//1000
    a %= 1000
    seang += a//100
    a %= 100
    seang += a//10
    a %= 10
    seang += a
    if N == seang:
        print(i)
        break
else:
    print(0)