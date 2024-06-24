function solution(phone_number) {
    var lastNum = phone_number.substring(phone_number.length - 4, phone_number.length)
    
    return lastNum.padStart(phone_number.length, "*");
}