function solution(arr) {
    let num = 1;
    while(num < arr.length) num *= 2;
    
    for(let i = 0; i<num; i++){
        if(arr[i] === undefined) arr.push(0)
    }
    return arr;
}