import sys
N = int(input())
user = iter(sys.stdin.read().strip().split())
user1 = [(int(a), b) for a, b in zip(user, user)]
user1.sort(key=lambda x:x[0])
for a, b in user1:
    print(a, b)