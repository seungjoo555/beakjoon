number = int(input())

for i in range(number):
    print(" " * i + "*" * ((number*2-1)-(i*2)))