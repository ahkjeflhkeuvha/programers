function solution(n_str) {
    while(n_str.indexOf('0') == 0){
        n_str = n_str.replace('0', "")
    }
    return n_str;
}