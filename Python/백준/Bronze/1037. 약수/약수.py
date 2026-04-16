import sys
input = sys.stdin.readline

num = int(input())
primeList = list(map(int, input().strip().split()))
maxPrime = max(primeList)
minPrime = min(primeList)
if num == 1:
    maxPrime **= 2
else:
    maxPrime = maxPrime * minPrime

print(maxPrime)