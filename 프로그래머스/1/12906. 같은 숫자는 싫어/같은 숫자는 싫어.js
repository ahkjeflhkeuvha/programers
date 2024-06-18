function solution(arr)
{
    var answer = [];

    arr.forEach((val, idx)=>{
        if(answer[answer.length - 1] != val) answer.push(val)
    })
    
    return answer;
}