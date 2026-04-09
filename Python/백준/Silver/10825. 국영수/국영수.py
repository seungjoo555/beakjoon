import sys
N = int(input())
student = iter(sys.stdin.read().split())
student1 = [[a, int(b), int(c), int(d)] for a, b, c, d in zip(student, student, student, student)]
student1.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
for a in student1:
    print(a[0])


