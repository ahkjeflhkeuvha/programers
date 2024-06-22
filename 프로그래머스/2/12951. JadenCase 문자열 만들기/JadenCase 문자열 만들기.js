function solution(s) {
    let strArr = s.split(' ')
    strArr = strArr.map((val) => {
        return val.charAt(0).toUpperCase().concat(val.substring(1).toLowerCase())
    })

    return strArr.join(' ');
}