function solution(number, limit, power) {
    var divisorArr = []
    var tot = 0
    
    for(var i = 1; i<=number; i++){
        if(getDivisors(i) <= limit) tot += getDivisors(i)
        else tot += power
    }

    return tot;
}

function getDivisors(num){
    const divisors = [];
    for(let i = 1 ; i <= Math.sqrt(num) ; i++){
        if(num % i === 0) {
            divisors.push(i);
            if(num / i != i) divisors.push(num / i);
        }
    }

    return divisors.length;
}