def solution(park, routes):
    s = [0, 0]
    parkSize = [len(park)-1, len(park[0])-1]
    for w in park:
        if w.find('S') != -1:
            s[1] = w.find('S')
            break
        s[0] += 1
    for r in routes:
        x, y = r.split(" ")
        y = int(y)
        match x:
            case 'E':
                if s[1] + y > parkSize[1] or 'X' in park[s[0]][s[1]:s[1]+y+1]:
                    continue
                else:
                    s[1] += y
            case 'S':
                if s[0] + y > parkSize[0] or 'X' in [p[s[1]] for p in park[s[0]:s[0]+y+1]]:
                    continue
                else:
                    s[0] += y
            case 'W':
                if s[1] - y < 0 or 'X' in park[s[0]][s[1]-y:s[1]+1]:
                    continue
                else:
                    s[1] -= y
            case 'N':
                if s[0] - y < 0 or 'X' in [p[s[1]] for p in park[s[0]-y:s[0]+1]]:
                    continue
                else:
                    s[0] -= y
    return s