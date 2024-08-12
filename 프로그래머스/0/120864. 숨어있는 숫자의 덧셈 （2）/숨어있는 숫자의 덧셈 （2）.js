function solution(my_string) {
    var answer = 0;
    return my_string.split(/\D+/g).reduce((a,c)=> Number(c) + Number(a), 0)
}