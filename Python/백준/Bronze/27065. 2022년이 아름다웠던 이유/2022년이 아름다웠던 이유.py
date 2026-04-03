import sys
input = sys.stdin.readline
def getDivisor(n):

    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i)
            if ( (i**2) != n) : 
                divisorsList.append(n // i)
    divisorsList.remove(n)
    return divisorsList

def gb_boj2022(num):
    divList = getDivisor(num)
    if num < sum(divList):
        for i in divList:
            if i < sum(getDivisor(i)):
                return 0
        return 1
    else:
        return 0



T = int(input())

for _ in range(T):
    n = int(input())
    if gb_boj2022(n):
        print("Good Bye")
    else:
        print("BOJ 2022")