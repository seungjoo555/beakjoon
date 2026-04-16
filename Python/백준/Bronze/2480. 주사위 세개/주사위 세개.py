a, b, c = map(int, input().split())
prize = 0
if a == b and b == c:
    prize = a * 1000 + 10000
elif a == b or b == c or a == c:
    if a == b:
        prize = a * 100 +1000
    elif b == c:
        prize = b * 100 +1000
    elif a == c:
        prize = c * 100 +1000
else:
    max = a
    if max < b:
        max = b
    if max < c:
        max = c
    prize = max * 100
print(prize)