function solution(n) {
    return checkNum(n);
}

function checkNum(n){
    var cnt = 0;
    var boolArr = new Array(n + 1).fill(true);
    [boolArr[0], boolArr[1]] = [false, false];
    for(let i = 2; i<boolArr.length; i++){
        if(boolArr[i]) {
            for(var j = i*i; j<=n; j+=i) boolArr[j] =false;
        }
    }

    for(let i of boolArr){
        if(i) cnt++;
    }
    return cnt;
}