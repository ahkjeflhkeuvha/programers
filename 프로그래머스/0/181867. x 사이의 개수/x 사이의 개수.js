function solution(myString) {
    var answer = [];
    var arr = myString.split("x")
    
    for(str of arr){
        answer.push(str.length)
    }
    return answer;
}