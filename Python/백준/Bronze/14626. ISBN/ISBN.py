ISBN = (' '.join(input()).split())
check = ISBN.index('*')
for i in range(10):
    ISBN[check] = i
    ISBN = list(map(int, ISBN))
    if (sum(ISBN[0::2]) + (sum(ISBN[1::2]) * 3)) % 10 == 0:
        print(i)
        break