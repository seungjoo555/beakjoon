def solution(wallpaper):
    minX = 0
    minY = 0
    maxX = 0
    maxY = 0
    l = len(wallpaper[0])
    for i in range(len(wallpaper)):
        if wallpaper[i].count('#'):
            minY = i
            break
    minX = wallpaper[minY].find('#')
    maxX = l - wallpaper[minY][::-1].find('#')
    for i in range(minY, len(wallpaper)):
        if wallpaper[i].count('#'):
            maxY = i+1
        for j in range(l):
            x = wallpaper[i].find('#')
            y = wallpaper[i][::-1].find('#')
            if x < minX and x >= 0:
                minX = x
            if l - y > maxX and y >= 0:
                maxX = l - y
    answer = [minY, minX, maxY, maxX]
    print(answer)
    return answer