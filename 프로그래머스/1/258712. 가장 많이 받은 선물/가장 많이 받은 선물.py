def solution(friends, gifts):
    answer = 0
    giftPoint = [0 for _ in range(len(friends))]
    giftCount = [0 for _ in range(len(friends))]
    for i in range(len(gifts)):
        g, t = gifts[i].split()
        giftPoint[friends.index(g)] += 1
        giftPoint[friends.index(t)] -= 1
    print(giftPoint)

    for i in range(len(friends)-1):
        for j in range(i+1, len(friends)):
            g1 = friends[i]+" "+friends[j]
            g2 = friends[j]+" "+friends[i]
            if gifts.count(g1) == gifts.count(g2):
                if giftPoint[i] > giftPoint[j]:
                    giftCount[i] += 1
                elif giftPoint[i] < giftPoint[j]:
                    giftCount[j] += 1
            elif gifts.count(g1) > gifts.count(g2):
                giftCount[i] += 1
            else:
                giftCount[j] += 1
    answer = max(giftCount)
    return answer