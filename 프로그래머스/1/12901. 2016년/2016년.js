function solution(a, b) {
    var wholeWeek = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    var week = [5, 1, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    return wholeWeek[(week[a-1]+(b-1))%7];
}