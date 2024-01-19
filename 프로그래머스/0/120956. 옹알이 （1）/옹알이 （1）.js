function solution(babbling) {
    var answer = 0;

    for(let i = 0; i<babbling.length; i++){
        if(babbling[i].match("^(aya|ye|woo|ma)+$")) answer++;
    }
    return answer;
}