function solution(arr)
{
    var answer = [];
    for(let i = 0, val = -1; i<arr.length; i++){
        if(arr[i] != val) {
            answer.push(arr[i]);
            val = arr[i];
        }
    }
    
    return answer;
}