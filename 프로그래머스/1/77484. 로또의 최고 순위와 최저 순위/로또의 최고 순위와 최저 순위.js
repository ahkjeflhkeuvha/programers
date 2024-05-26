function solution(lottos, win_nums) {
    var answer = new Array(2);
    var cntZero = 0
    var cntRight = 0
    
    lottos.sort((a, b) => b-a)
    win_nums.sort((a, b) => b-a)
    
    for(var i = 0; i<lottos.length; i++) {
        if(lottos[i] == 0) cntZero++
        else if(win_nums.includes(lottos[i])) cntRight++
    }
    
    var maxScore = cntZero + cntRight
    var minScore = cntRight
    
    var score = [6, 5, 4, 3, 2]
    
    answer[0] = (score.indexOf(maxScore)) >= 0 ? score.indexOf(maxScore) + 1 : 6
    answer[1] = (score.indexOf(minScore)) >= 0 ? score.indexOf(minScore) + 1 : 6
    
    return answer;
}