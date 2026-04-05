import sys
input = map(int, sys.stdin.read().split())
N = next(input)
st = []
for _ in range(N):
    order = next(input)
    match order:
        case 1:
            x = next(input)
            st.append(x)
        case 2:
            if st:
                print(st.pop())
            else:
                print(-1)
        case 3:
            print(len(st))
        case 4:
            if st:
                print(0)
            else:
                print(1)
        case 5:
            if st:
                print(st[-1])
            else:
                print(-1)
