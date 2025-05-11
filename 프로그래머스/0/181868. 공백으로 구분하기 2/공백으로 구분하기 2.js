function solution(my_string) {
    var answer = my_string.trim().replace(/\s+/g, ' ').split(' ');
    return answer;
}