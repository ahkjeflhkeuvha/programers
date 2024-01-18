function solution(arr, k) {
    return [...Array.from(new Set(arr)), ...new Array(k).fill(-1)].slice(0, k);
}