function solution(arr) {
    var min = Math.min(...arr)
    return arr.filter((a) => a != min).length == 0 ? new Array(1).fill(-1) : arr.filter((a) => a != min)  ;
}