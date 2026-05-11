def solution(left, right):
    import math
    def count_divisors_fast(n):
        divisors = []
        # 제곱근까지만 반복
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                divisors.append(i)
                # 짝이 되는 약수 추가 (중복 방지)
                if i != n // i:
                    divisors.append(n // i)
        return len(divisors)
    answer = 0
    num = []
    divisor = []
    for i in range(left, right+1):
        num.append(i)
        divisor.append(count_divisors_fast(i))
    for i in range(len(num)):
        if divisor[i]&1 == 0:
            answer += num[i]
        else:
            answer -= num[i]
    return answer