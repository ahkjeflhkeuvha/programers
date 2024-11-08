function solution(new_id) {
    var answer = '';
    answer = new_id.toLowerCase().match(/[a-z0-9-_.]/g).join('').replace(/\.+/g, ".")

    if(answer.startsWith(".")) answer = answer.substring(1, answer.length)
    else if(answer.endsWith(".")) answer = answer.substring(0, answer.length - 1)
    
    if(answer.length === 0) answer = "a"
    else if(answer.length >= 16) answer = answer.substr(0, 15)
    
    if(answer.endsWith(".")) answer = answer.substring(0, answer.length - 1)
    
    while(answer.length <= 2) answer += answer[answer.length - 1]
    
    return answer;
}