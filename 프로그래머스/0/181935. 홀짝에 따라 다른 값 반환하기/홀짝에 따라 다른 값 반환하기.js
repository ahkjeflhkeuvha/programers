function solution(n) {
    return n%2 == 0 ? even(n) : odd(n);
}
function odd(n){
    let res = 0;
    for(let i = 1; i<=n; i+=2)
        res += i;
    return res;
}
function even(n){
    let res = 0;
    for(let i = 0; i<=n; i+=2)
        res += i**2;
    return res;
}