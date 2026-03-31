import math
import sys
input = sys.stdin.readline

def get_primes(n):
    sieve = [True] * (n + 1)
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return [p for p in range(2, n + 1) if sieve[p]]

superPrime = get_primes(318137)
T = int(input())
for i in range(T):
    n = int(input())
    print(superPrime[superPrime[n-1]-1])