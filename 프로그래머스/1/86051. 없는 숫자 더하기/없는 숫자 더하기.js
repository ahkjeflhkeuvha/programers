function solution(numbers) {
    var answer = 0;
    var str = "0123456789";
    
    for(let i = 0; i<numbers.length; i++){
        if(str.includes(String(numbers[i]))) answer += numbers[i];
    }
    return 45- answer;
}