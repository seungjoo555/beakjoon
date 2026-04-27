import sys

# 입력 속도를 높이기 위해 sys.stdin.readline 사용
input = sys.stdin.read

def solve():
    # 전체 입력을 한 번에 받아와서 줄 단위로 분리
    data = input().splitlines()
    
    # 초기 문자열을 왼쪽 스택에 담음
    # 커서는 처음에 문장 맨 뒤에 있으므로 모든 문자는 커서 왼쪽에 존재
    left_stack = list(data[0])
    right_stack = []
    
    # 명령어의 개수
    m = int(data[1])
    
    # 3번째 줄부터 실제 명령어 시작
    for i in range(2, 2 + m):
        command = data[i]
        
        # 커서를 왼쪽으로 한 칸 옮김
        if command == 'L':
            if left_stack:
                # 커서가 왼쪽으로 가므로, 왼쪽 스택의 마지막 문자가 커서 오른쪽으로 넘어감
                right_stack.append(left_stack.pop())
                
        # 커서를 오른쪽으로 한 칸 옮김
        elif command == 'D':
            if right_stack:
                # 커서가 오른쪽으로 가므로, 오른쪽 스택의 마지막 문자가 커서 왼쪽으로 넘어감
                left_stack.append(right_stack.pop())
                
        # 커서 왼쪽에 있는 문자를 삭제
        elif command == 'B':
            if left_stack:
                left_stack.pop()
                
        # 커서 왼쪽에 새로운 문자 추가 (P $)
        elif command.startswith('P'):
            # "P x" 형태이므로 공백 뒤의 문자만 추출
            _, char = command.split()
            left_stack.append(char)
            
    # 출력을 위해 두 스택을 합침
    # right_stack은 뒤집혀 있는 상태(커서와 가까운 쪽이 top)이므로 뒤집어서 출력
    result = "".join(left_stack) + "".join(reversed(right_stack))
    print(result)

if __name__ == "__main__":
    solve()