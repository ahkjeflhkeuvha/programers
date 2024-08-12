function solution(my_string) {
    return my_string.split("").map((a)=>parseInt(a)).filter((a)=>Number.isInteger(a)).reduce((a,c) => (a+c))
}