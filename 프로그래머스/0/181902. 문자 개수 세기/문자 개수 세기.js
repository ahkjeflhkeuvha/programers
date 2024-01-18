function solution(my_string) {
    var answer = new Array(52).fill(0);
    for(let i = 0; i<my_string.length; i++){
        if(my_string.charCodeAt(i) >= 97 && my_string.charCodeAt(i) <= 122) answer[my_string.charCodeAt(i) - 71]++;
        else answer[my_string.charCodeAt(i) - 65]++;
    }
    return answer;
}