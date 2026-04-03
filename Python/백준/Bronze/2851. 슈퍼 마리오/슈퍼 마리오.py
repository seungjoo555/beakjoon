import sys
inp = map(int, sys.stdin.read().split())
mush = [*inp]
def sum(mush):
    sum = 0
    for i in mush:
        sum += i
        if sum == 100:
            print(sum)
            return
        elif sum > 100:
            if abs(sum-100) == abs(sum-100-i):
                print(sum)
                return
            elif abs(sum-100) > abs(sum-100-i):
                print(sum-i)
                return
            else:
                print(sum)
                return
    print(sum)
sum(mush)