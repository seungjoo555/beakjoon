import math
import sys
input = sys.stdin.readline

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

superPrime = []
check = 1
for i in range(3,318138,2):
        if is_prime(i):
            check += 1
            if is_prime(check):
                superPrime.append(i)
T = int(input())
for i in range(T):
    n = int(input())
    print(superPrime[n-1])