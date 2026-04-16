while True:
    n = int(input())
    sum = 0
    string = ""
    if n == -1:
        break
    for i in range(1, n//2+1):
        if n % i == 0:
            sum += i
            if string == "":
                string = (f" = {i}")
            else:
                string = string + (f" + {i}")
    if sum == n:
        print(f"{n}{string}")
    else:
        print(f"{n} is NOT perfect.")