def solution(wallpaper):   
    lux, luy, rdx, rdy = float('inf'), float('inf'), float('-inf'), float('-inf')

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                lux = min(i, lux)
                luy = min(j, luy)
                rdx = max(i, rdx)
                rdy = max(j, rdy)
                
    return [lux, luy, rdx+1, rdy+1]