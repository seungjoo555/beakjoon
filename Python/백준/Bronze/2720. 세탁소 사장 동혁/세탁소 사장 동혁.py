def fuc():
    import sys
    input = map(int, sys.stdin.read().split())
    T = next(input)
    for i in range(T):
        C = next(input)
        Q = C//25
        D = C%25//10
        N = C%25%10//5
        P = C%25%10%5
        print(Q, D, N, P)

fuc()