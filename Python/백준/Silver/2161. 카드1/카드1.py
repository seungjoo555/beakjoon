import sys
input = sys.stdin.readline

N = int(input())
card = [i for i in range(1, N+1)]
throw = []

while len(card) > 1:
    throw.append(card.pop(0))
    card.append(card.pop(0))

for i in throw:
    print(i, end = " ")
print(card[0])