function solution(s) {
    var answer = '';
    var strArr = s.split(" ")
    
    for (var strItem of strArr){
        for(var idx in strItem){
            if(idx%2 == 0) answer += strItem[idx].toUpperCase()
            else answer += strItem[idx].toLowerCase()
        }
        answer += ' '
    }
    return answer.slice(0, s.length);
}