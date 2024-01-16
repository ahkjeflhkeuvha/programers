function solution(quiz) {
    var answer = [];
    for(let i = 0; i<quiz.length; i++){
        let str = eval(quiz[i].split(" = ")[0]) == quiz[i].split(" = ")[1] ? "O" : "X";
        answer.push(str);
    }
    return answer;
}