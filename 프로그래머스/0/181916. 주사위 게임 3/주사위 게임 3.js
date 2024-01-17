function solution(a, b, c, d) {
    var arr = [a, b, c, d];
    arr.sort();
    
    if(arr[0] == arr[3]) return 1111 * arr[0];
    else if(arr[0] == arr[2] || arr[1] == arr[3]) return Number(Math.pow((arr[1] * 10)  + arr[0] + arr[3] - arr[1], 2));
    else if(arr[0] == arr[1] && arr[2] == arr[3]) return (arr[0] + arr[2]) * (arr[2] - arr[0]);
    else if(arr[0] == arr[1]) return arr[2] * arr[3];
    else if(arr[1] == arr[2]) return arr[0] * arr[3];
    else if(arr[2] == arr[3]) return arr[0] * arr[1];
    else return arr[0];
}