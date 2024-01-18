function solution(arr) {
    const [row, col] = [arr.length, arr[0].length];
    if(row === col) return arr;
    else if(row < col) return [...arr, ...new Array(col - row).fill().map(() => new Array(col).fill(0))];
    else return arr.map((r) => [...r, ...new Array(row - col).fill(0)]);
}