a, b = None, None
while a != 0 and b != 0:
    a, b = map(int, input().split())
    if(a == 0 and b == 0): break
    print(a+b)