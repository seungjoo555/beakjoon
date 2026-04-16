import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_divisor_list(n):
    dList = []
    for i in range(1, n//2+1):
        if n % i == 0:
            dList.append(i)
    dList.append(n)
    return dList

n = int(input())
number = list(map(int, input().split()))
number.sort()
a = gcd(number[0], number[1])
if n == 3:
    a = gcd(a, number[2])
for i in get_divisor_list(a):
    print(i)