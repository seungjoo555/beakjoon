def so():
    import sys
    input = map(int, sys.stdin.read().split())
    n = next(input)
    st = []
    pm = []
    c = 1
    for num in input:
        while num >= c :
            st.append(c)
            pm.append("+")
            c += 1
        if st.pop() == num:
            pm.append("-")
        else:
            return print("NO")
    print('\n'.join(pm))
so()