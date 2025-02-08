import itertools

def chk_dungeons(k, dungeons):  
    max_dungeon = 0
    for dungeon in dungeons:
        min_fatigue, use_fatigue = dungeon
        if k < min_fatigue:
            return max_dungeon
        else:
            max_dungeon += 1
            k -= use_fatigue
    return max_dungeon

def solution(k, dungeons):
    answer = 0
    
    for dungeon in list(itertools.permutations(dungeons, len(dungeons))):
        res = chk_dungeons(k, dungeon)
        answer = max(answer, res)
    return answer