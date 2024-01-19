function solution(rank, attendance) {
    var arr = [];
    
    for(let i = 0; i<rank.length; i++){
        if(attendance[i] == true) arr.push(rank[i]);
    }
    arr.sort((a, b) => a - b);
    
    return rank.indexOf(arr[0]) * 10000 + rank.indexOf(arr[1]) * 100 + rank.indexOf(arr[2]);
}