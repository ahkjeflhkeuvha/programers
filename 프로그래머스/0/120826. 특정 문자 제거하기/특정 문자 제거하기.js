function solution(my_string, letter) {
    const exp = new RegExp(`${letter}`, 'g');
    return my_string.replace(exp, "");
}