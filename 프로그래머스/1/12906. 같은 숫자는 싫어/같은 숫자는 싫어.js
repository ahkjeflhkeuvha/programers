function solution(arr)
{
    var answer = [];
    
    arr.forEach((val, idx) => {
        if(check(val, idx, [...arr])) answer.push(val);
    })
    return answer;
}

function check(val, idx, arr){
    if(val != arr[idx + 1]) return true;
    else return false;
}