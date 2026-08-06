def solution(clothes):
    answer = 0
    clothType = []
    clothTypeCount = []
    clothTypeSet = set()
    for c in clothes:
        clothType.append(c[1])
        clothTypeSet.add(c[1])
    clothTypeSetList = list(clothTypeSet)
    for cl in clothTypeSetList:
        clothTypeCount.append(clothType.count(cl))

    answer = clothTypeCount[0]+1
    for i in range(1, len(clothTypeCount)):
        answer *= clothTypeCount[i]+1

    return answer - 1