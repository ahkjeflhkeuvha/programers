def solution(dirs):
    answer = 0
    location = set()
    x, y = 0, 0
    
    loc_dic = {'U' : [0, 1], 'D': [0, -1], 'R': [1, 0], 'L' : [-1, 0]}
    
    for loc in dirs:
        dx = x + loc_dic[loc][0]
        dy = y + loc_dic[loc][1]
        
        if -5 <= dx <= 5 and -5 <= dy <= 5:
            location.add((x, y, dx, dy))
            location.add((dx, dy, x, y))
            x, y = dx, dy
            
    print(location)
    return len(location) // 2