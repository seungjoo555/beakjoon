import math

def is_prime_number_v2(N):
    if N == 1 : return
    for i in range(2, N//2+1):
        if N % i == 0:
            return 
    return N
    
def is_prime_number_v3(N):
    if N == 1 : return True
    sqrt = math.sqrt(N)
    prime_list = []
    for i in range(2, int(sqrt)+1):
        if is_prime_number_v2(i) != None:
            prime_list.append(is_prime_number_v2(i))
    for p in prime_list:
        if N % p == 0: return False
    return True

string = list(input())
sum = 0
for ch in string:
    if ord(ch) - 96 < 0:
        sum += ord(ch) - 38
    else:
        sum += ord(ch) - 96

if is_prime_number_v3(sum):
    print("It is a prime word.")
else:
    print("It is not a prime word.")