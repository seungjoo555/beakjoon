ISBN = (input())
check = ISBN.index('*')
a = ' '.join(ISBN[0:12:2]).split()
b = ' '.join(ISBN[1::2]).split()
if check == 12:
    a = list(map(int, a))
    b = list(map(int, b))
    for i in range(10):
        if (sum(a) + (sum(b)*3) + i) % 10 == 0:
            print(i)
            break
elif check%2 == 0:
    a.remove('*')
    a = list(map(int, a))
    b = list(map(int, b))
    for i in range(10):
        if (sum(a)+ i + (sum(b)*3) + int(ISBN[-1])) % 10 == 0:
            print(i)
            break
else:
    b.remove('*')
    a = list(map(int, a))
    b = list(map(int, b))
    for i in range(10):
        if (sum(a) + ((sum(b)+ i)*3) + int(ISBN[-1])) % 10 == 0:
            print(i)
            break