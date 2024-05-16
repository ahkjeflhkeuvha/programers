function solution(strings, n) {
    var answer = [];
    answer = strings.sort((a, b)=>{
        if(a[n] < b[n]) return -1
        else if(a[n] == b[n]) return a.localeCompare(b)
        else return 0
    })
    return answer;
}