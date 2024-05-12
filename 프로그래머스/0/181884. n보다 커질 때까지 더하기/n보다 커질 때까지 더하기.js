function solution(numbers, n) {
    var answer = 0
    var i = 0
    
    while(answer <= n){
        answer += numbers[i++]
    }
    return answer;
}