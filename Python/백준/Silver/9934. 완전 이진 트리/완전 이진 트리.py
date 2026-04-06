import sys
input = map(int, sys.stdin.read().split())
K = next(input)
input = list(input)
st = []
for i in range(K):
    st.append(input[0::2])
    input = input[1::2]
for i in range(K):
    print(' '.join(map(str, st[-(i+1)])))