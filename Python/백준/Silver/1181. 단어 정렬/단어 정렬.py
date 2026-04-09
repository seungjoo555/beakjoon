import sys
N = int(input())
word = list(set(sys.stdin.read().strip().split()))
word.sort(key=lambda x:(len(x), x))
print('\n'.join(word))