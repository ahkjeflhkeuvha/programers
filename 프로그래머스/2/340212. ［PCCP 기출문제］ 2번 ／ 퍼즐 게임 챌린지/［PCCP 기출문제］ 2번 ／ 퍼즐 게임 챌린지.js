
function chk_time(diffs, times, limit, level) {
    let totalTime = 0
    
    for(let i in diffs) {
        let cur_diff = diffs[i]
        let cur_time = times[i]
        
        if(cur_diff <= level) totalTime += cur_time
        else {
            let prev_time = times[i-1]
            totalTime += (prev_time + cur_time) * (cur_diff - level) + cur_time
        }
        
        if (totalTime > limit) return false
    }
    return true
}

function solution(diffs, times, limit) {
    let left = 1
    let right = [...diffs].sort((a, b) => b - a)[0]
    
    while(left <= right) {
        let mid = Math.floor((left + right) / 2)
        let res = chk_time(diffs, times, limit, mid)
        
        if(res) right = mid - 1
        else left = mid + 1
        
    }
    return left;
}