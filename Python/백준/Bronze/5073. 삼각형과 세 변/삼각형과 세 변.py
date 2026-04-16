import sys
input = sys.stdin.readline

while True:
    t1, t2, t3 = map(int, input().split())

    if t1 == 0 and t2 == 0 and t3 == 0:
        break
    
    sum = t1 + t2 + t3
    c2 = sum - t2
    c3 = sum - t3
    c1 = sum - t1
    if t1 >= c1 or t2 >= c2 or t3 >= c3:
        print("Invalid")

    elif t1 == t2 and t2 == t3:
        print("Equilateral")
    
    elif t1 == t2 or t2 == t3 or t1 == t3:
        print("Isosceles")

    else:
        print("Scalene")