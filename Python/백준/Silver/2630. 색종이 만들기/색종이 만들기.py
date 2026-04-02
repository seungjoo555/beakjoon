import sys
input = sys.stdin.readline
N = int(input())
paper = []
color_list = []

for _ in range(N):
    paper.append(list(map(int, input().split())))

def makePaper(row, col, size):
    color = paper[row][col]
    for i in range(row, row+size):
        for j in range(col, col+size):
            if paper[i][j] != color:
                new_size = size // 2
                makePaper(row, col, new_size)
                makePaper(row, col+new_size, new_size)
                makePaper(row+new_size, col, new_size)
                makePaper(row+new_size, col+new_size, new_size)
                return
    color_list.append(color)

makePaper(0, 0, N)
print(color_list.count(0))
print(color_list.count(1))