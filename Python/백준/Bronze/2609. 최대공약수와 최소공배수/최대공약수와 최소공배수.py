import sys
input = sys.stdin.readline
def get_lcm(M, N):
    if M > N : M, N = N, M

    i = 1
    while True:
        multiple = N * i
        if multiple % M == 0:
            return multiple
        i += 1

def get_gcd(M, N):
    if M > N : M, N = N, M

    for num in range(M, 0, -1):
        if M % num == 0 and N % num == 0:
            return num

A, B = map(int, input().split())
print(get_gcd(A, B))
print(get_lcm(A, B))