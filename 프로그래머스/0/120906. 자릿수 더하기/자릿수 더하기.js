function solution(n) {
    var answer = 0;
    String(n).split("").forEach((i) => {answer += Number(i)});
    return answer;
}