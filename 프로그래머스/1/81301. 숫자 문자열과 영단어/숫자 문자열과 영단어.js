function solution(s) {
    var alphabet = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    alphabet.forEach((val, idx) => s = s.replaceAll(val, idx))
    return +s;
}