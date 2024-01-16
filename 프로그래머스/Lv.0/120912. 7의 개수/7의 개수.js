function solution(array) {
    return array.join('').split("").filter(str => str === "7").length;;
}