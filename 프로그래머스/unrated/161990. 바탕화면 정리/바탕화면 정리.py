def solution(wallpaper):
    answer = []
    tmp = []
    height = []
    width = []

    for h in range(len(wallpaper)) :
        for w in range(len(wallpaper[h])) :
            if wallpaper[h][w] == '#' :
                height.append(h)
                width.append(w)
                #print('h:',h,',w:',w)
    answer.append(min(height))
    answer.append(min(width))
    answer.append(max(height)+1)
    answer.append(max(width)+1)
    
    return answer