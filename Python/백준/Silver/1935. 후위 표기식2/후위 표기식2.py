import sys

# 1. 입력 받기
n = int(sys.stdin.readline())
expression = sys.stdin.readline().strip()
values = [int(sys.stdin.readline()) for _ in range(n)]

stack = []

# 2. 후위 표기식 계산
for char in expression:
    if 'A' <= char <= 'Z':
        # 피연산자라면 해당되는 숫자를 스택에 추가
        stack.append(values[ord(char) - ord('A')])
    else:
        # 연산자라면 스택에서 숫자 두 개를 꺼냄
        num2 = stack.pop()
        num1 = stack.pop()
        
        if char == '+':
            stack.append(num1 + num2)
        elif char == '-':
            stack.append(num1 - num2)
        elif char == '*':
            stack.append(num1 * num2)
        elif char == '/':
            stack.append(num1 / num2)

# 3. 최종 결과 출력 (소수점 둘째 자리까지)
print(f"{stack[0]:.2f}")