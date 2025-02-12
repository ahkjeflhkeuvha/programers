function solution(schedules, timelogs, startday) {
    var answer = 0;
    let member = schedules.length
    let chkMember = Array.from(Array(member), () => new Array(7).fill(null))
    
    for(let j = 0; j<7; j++) {        
        for(let i = 0; i<member; i++){
            schedules[i] = schedules[i].toString().padStart(4, '0')
            let hour = Number(schedules[i].substr(0, 2))
            let minute = Number(schedules[i].substr(2, 2)) + 10
            
            if (minute >= 60) {
                hour += 1
                minute %= 60
            }
            let maximum = hour*100 + minute
            let attendTime = timelogs[i][j]
            
            if(attendTime <= maximum) {
                chkMember[i][(startday-1)%7] = true
            } else {
                chkMember[i][(startday-1)%7] = false
            }
        }
        startday++
    }

    answer = member
    for(let i = 0; i<member; i++){
        for(let j = 0; j<5; j++){
            if(chkMember[i][j] == false) {
                answer--
                break
            }
        }
    }
    return answer;
}