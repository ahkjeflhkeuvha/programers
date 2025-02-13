function solution(number, k) {
    var answer = '';
    let stack = []
    
    for(let i in number) {
        let current = number[i]
        
        while(k > 0 && stack.length > 0 && stack[stack.length - 1] < current) {
            stack.pop()
            k--
        }
        
        stack.push(current)
    }

    return stack.join('').slice(0, number.length - k);
}