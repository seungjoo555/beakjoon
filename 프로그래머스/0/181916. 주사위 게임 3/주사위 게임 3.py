def solution(a, b, c, d):
    answer = 0
    dice = [a, b, c, d]
    check = list(set(dice))

    match len(check):
        case 1:
            answer = a * 1111
        case 2:
            ea = dice.count(check[0])
            if ea in [1, 3]:
                if ea == 3:
                    answer = (10*check[0]+check[1]) ** 2
                else:
                    answer = (10*check[1]+check[0]) ** 2
            else:
                answer = ((check[0] + check[1]) * abs(check[0] - check[1]))
        case 3:
            for i in check:
                dice.remove(i)
            check.remove(dice[0])
            answer = check[0] * check[1]
        case 4:
            answer = min(dice)

    return answer