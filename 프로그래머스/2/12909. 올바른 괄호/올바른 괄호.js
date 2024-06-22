function solution(s){
    var answer = true;
    var stack = []
    
    for(var str of s){
        if(str == '(') stack.push(str)
        else {
            if(stack.length == 0) return false
            stack.pop()
        }
    }

    return (stack.length) ? false : true;
}