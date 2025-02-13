function solution(sequence, k) {
    var answer = [];
    let n = sequence.length
    let left = 0
    let right = 0
    let sum = sequence[0]
    let min_len = Number.MAX_SAFE_INTEGER
    
    while(right < n) {
        if(sum == k) {
            if(right - left + 1 < min_len){
                min_len = right - left + 1
                answer = [left, right]
            }
        }
        
        if(sum >= k) {
            sum -= sequence[left]
            left += 1
        }
        else {
            right += 1
            if(right < n) sum += sequence[right]
        }
    }
    return answer;
}