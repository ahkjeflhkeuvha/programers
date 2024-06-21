function solution(arr) {
    let i = 0
    while(arr.length > Math.pow(2, i)) {
        i++
    }
    
    let len = Math.pow(2, i) - arr.length
    arr = arr.concat(new Array(len).fill(0))

    return arr;
}
