function solution(babbling) {
    var answer = 0;
    var text = ['ma', 'woo', 'aya', 'ye'];
    
    for(let i = 0; i<babbling.length; i++){
        for(let j = 0; j<text.length; j++){
            babbling[i] = babbling[i].replace(text[j], ' ');
        }
        if(babbling[i].trim() == 0) answer++;
    }
    
    return answer;
}