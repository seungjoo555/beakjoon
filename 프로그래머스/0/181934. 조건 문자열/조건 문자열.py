def solution(ineq, eq, n, m):
    eq = "=" if eq == "=" else ""
    answer = 1 if eval(str(n)+ineq+eq+str(m)) else 0
    return answer