import math

def is_prime_number_v2(N):
    if N == 1 : return
    for i in range(2, N//2+1):
        if N % i == 0:
            return 
    return N
    
def is_prime_number_v3(N):
    if N == 1 : return False
    sqrt = math.sqrt(N)
    prime_list = []
    for i in range(2, int(sqrt)+1):
        if is_prime_number_v2(i) != None:
            prime_list.append(is_prime_number_v2(i))
    for p in prime_list:
        if N % p == 0: return False
    return True

N = int(input())
if is_prime_number_v3(N):
    print(N)
else:
    i = 2
    while N > 0:
        if N == 1:
            break
        if N % i == 0:
            N //= i
            print(i)
        else:
            i += 1