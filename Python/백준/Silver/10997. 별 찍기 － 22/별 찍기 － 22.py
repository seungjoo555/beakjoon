import sys

def solve():
    n = int(sys.stdin.readline())

    # N이 1인 경우는 예외적으로 별 하나만 출력
    if n == 1:
        print("*")
        return

    # 소용돌이의 전체 크기 계산
    width = 4 * n - 3
    height = 4 * n - 1

    # 전체를 공백으로 채운 2차원 배열 초기화
    board = [[' ' for _ in range(width)] for _ in range(height)]

    # 시작 위치 (우측 상단 끝)
    x, y = 0, width - 1
    
    # 별을 그리는 방향: 왼쪽, 아래, 오른쪽, 위
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    
    # 초기 방향: 왼쪽
    direction = 0
    
    # 첫 줄의 길이는 가로 길이 전체
    # 이후 아래로 2칸, 오른쪽으로 2칸... 이런 식으로 길이가 변함
    # 규칙상 첫 번째(왼쪽)와 두 번째(아래쪽) 이동 거리는 특별함
    lengths = [width - 1, height - 1]
    # 그 이후부터는 2, 2, 2... 씩 줄어드는 거리들을 추가
    for i in range(width - 1, 1, -2):
        lengths.append(i)
        lengths.append(i)

    # 시작점에 별 찍기
    board[x][y] = '*'

    for length in lengths:
        for _ in range(length):
            x += dx[direction]
            y += dy[direction]
            board[x][y] = '*'
        # 방향 전환 (0 -> 1 -> 2 -> 3 -> 0 ...)
        direction = (direction + 1) % 4

    # 결과 출력
    for i in range(height):
        # N=2 이상일 때, 두 번째 줄은 별이 하나만 있으므로 
        # rstrip()을 써서 불필요한 오른쪽 공백을 제거해야 함
        print("".join(board[i]).rstrip())

solve()