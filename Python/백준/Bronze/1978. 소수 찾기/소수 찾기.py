import sys
input = sys.stdin.readline
def is_prime_number(N):
    if N == 1 : return False
    for i in range(2, N):
        if N % i == 0:
            return False
    return True

N = int(input())
nlist = list(map(int, input().split()))
count = 0
for n in nlist:
    if is_prime_number(n):
        count += 1
print(count)