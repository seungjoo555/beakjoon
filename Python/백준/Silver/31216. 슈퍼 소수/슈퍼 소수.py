import math
import sys
input = sys.stdin.readline

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

superPrime = [3]
check = 2
T = int(input())
for i in range(T):
    n = int(input())
    while n > len(superPrime):
        for i in range(superPrime[-1]+2,318138,2):
            if is_prime(i):
                check += 1
                if is_prime(check):
                    superPrime.append(i)
                    break
    print(superPrime[n-1])