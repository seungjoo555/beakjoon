import sys
input = sys.stdin.readline
L = int(input())
S = input().strip()
print(S.count('A')*S.count('C')*S.count('G')*S.count('T')%1000000007)