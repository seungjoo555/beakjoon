a = int(input())
b = int(input())
c = int(input())
d = a + b + c
if d == 180 and (a == b and b == c):
    print("Equilateral")
elif d == 180 and (a == b or b == c or c == a):
    print('Isosceles')
elif d == 180:
    print("Scalene")
else:
    print("Error")