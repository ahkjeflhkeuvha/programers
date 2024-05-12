function solution(arr) {
    var answer = [];
    answer = arr.map((val)=>{
        if(val >= 50 && val%2 == 0) return val /= 2
        else if(val<50 && val%2 == 1) return val *= 2
        else return val
    })
    return answer;
}