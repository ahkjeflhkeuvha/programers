function solution(numbers) {
    var answer = new Array(numbers.length).fill(-1);
    var stack = [0, ]
    
    for(let i = 1; i<numbers.length; i++) {
        while(stack) {
            let idx = stack.pop()
            
            if(numbers[idx] < numbers[i]) answer[idx] = numbers[i]
            else {
                stack.push(idx)
                break
            }
        }
        stack.push(i)
    }
    return answer;
}