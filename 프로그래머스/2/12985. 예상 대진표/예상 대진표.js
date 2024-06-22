function solution(n,a,b)
{
    var answer = 1;

    for(var i = 0; i < Math.sqrt(n, 2); i++){
        a = Math.round(a/2)
        b = Math.round(b/2)
        
        answer++
        if(a == b) break;
    }
    

    return answer - 1;
}