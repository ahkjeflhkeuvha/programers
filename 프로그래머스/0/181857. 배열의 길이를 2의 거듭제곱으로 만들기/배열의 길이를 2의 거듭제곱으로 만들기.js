function solution(arr) {
    let i = 0;
    while (arr.length > Math.pow(2, i)) {
        i++;
    }

    let padLength = Math.pow(2, i);
    let padArr = new Array(padLength).fill(0);
    for (let j = 0; j < arr.length; j++) {
        padArr[j] = arr[j];
    }
    return padArr;
}
