def solution(genres, plays):
    answer = []
    playM = {}
    genreM = {}
    
    for i in range(len(genres)):
        if genres[i] not in playM:
            playM[genres[i]] = plays[i]
            genreM[genres[i]] = [[plays[i], i]]
        else:
            playM[genres[i]] += plays[i]
            genreM[genres[i]].append([plays[i], i])
           
    playM = sorted(playM.items(), key=lambda x: -x[1])
    
    for key, val in playM:
        data = sorted(genreM[key], key=lambda x: -x[0])[:2]
        answer.extend([idx for plays, idx in data])
    
    return answer