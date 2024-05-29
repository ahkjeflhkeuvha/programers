function solution(n, m, section) {
    var answer = 0;

    var i = section[0] - 1
  
    while(i < n){
        if(section.includes(i+1)){
            answer += 1
            i += m
        } 
        else i+=1
    }
        

    return answer;
}