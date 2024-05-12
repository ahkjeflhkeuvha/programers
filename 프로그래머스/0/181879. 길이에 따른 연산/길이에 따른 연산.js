function solution(num_list) {
    var answer = 0;
    if(num_list.length >= 11) answer = num_list.reduce((a,c)=> c += a)
    else answer = num_list.reduce((a,c) => c *= a)
    return answer;
}