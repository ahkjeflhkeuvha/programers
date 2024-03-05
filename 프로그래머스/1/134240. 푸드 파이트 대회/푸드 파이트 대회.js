function solution(food) {
    var answer = '';
    
    for(let i = 0; i<food.length; i++){
        if(Math.floor(food[i]/2) > 0){
            for(let j = 0; j<Math.floor(food[i]/2); j++) answer += i;
        }
    }
    return answer + '0' + answer.split("").reverse().join('');
}