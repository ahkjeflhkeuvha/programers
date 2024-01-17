function solution(my_string, overwrite_string, s) {
    var str = my_string.substring(0, s);
    var end = my_string.substring(s+overwrite_string.length);
    return str + overwrite_string + end;
}