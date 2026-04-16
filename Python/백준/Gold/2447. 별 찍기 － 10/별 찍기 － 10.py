import sys
n = int(sys.stdin.readline())
def so(n):
    if n == 1: return '*'
    star = so(n//3)
    st =[]
    for s in star:
        st.append(s*3)
    for s in star:
        st.append(s+' '*(n//3)+s)
    for s in star:
        st.append(s*3)
    return st

for s in so(n):
    print(s)