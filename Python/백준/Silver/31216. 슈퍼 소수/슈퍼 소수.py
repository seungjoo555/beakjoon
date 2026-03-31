import sys
input = sys.stdin.readline
def get_prime_primes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    primes = [p for p in range(2, n + 1) if sieve[p]]
    prime_primes = [
        primes[i]
        for i in range(len(primes))
        if sieve[i + 1]
    ]
    return prime_primes
T = int(input())
superPrime = get_prime_primes(318137)
for _ in range(T):
    n = int(input())
    print(superPrime[n-1])