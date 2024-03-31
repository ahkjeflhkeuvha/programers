function solution(strArr) {
    var answer = [];
    for(arr of strArr){
        if(arr.includes("ad")) continue
        answer.push(arr)
    }
    return answer;
}